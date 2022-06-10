from asyncio import start_unix_server
from cgitb import small
from enum import Enum
from nis import match
from re import S

#状態を列挙
class Status(Enum):
    Waiting = 0
    Blind = 1
    Cheched = 2
    Called = 3
    Raised = 4
    Folded = 5
    Allin = 6

#そのフェイズでの行動状態を列挙
class Action(Enum):
    Stand = 0
    taken = 1

#ポーカーにおける位置を列挙
class Position(Enum):
    DealerButton = 0
    SmallBlind = 1
    BigBlind = 2
    UnderTheGun = 3
    HighJack = 4
    CutOff = 5
 
#ゲームの設定のクラス　現在はsb_valueのみ活用
class Setting():

    def __init__(self):
        self.sb_value = None
        self.game_count = None
        self.turn = 0
        self.turn_player_status = Status.Waiting
        self.min_bet = 0
        self.call_need = 0
        self.raise_before = 0
        self.main_pot = 0

    #betの最小単位を設定
    def set_sb_value(self, value):
        self.sb_value = value

    #現在のプレイヤーの添字を設定
    def set_turn(self, turn):
        self.turn = turn

    #現在のプレイヤーの状態を設定
    def set_turn_player_status(self, status):
        self.turn_player_status = status

    #callに必要な額を設定
    def set_call_need(self, new_max):
        self.call_need = new_max

    #メインポットを設定する
    def set_main_pot(self,sum):
        self.main_pot = sum

    #ブラインドを設定する
    def update_blind(self, turn):
        self.raise_before = self.sb_value*2
        self.call_need = self.raise_before
        self.min_bet = self.call_need
        self.set_turn(turn)

    def update_raise_before(self, betting):
        before_call_need = self.call_need
        self.set_call_need(betting)
        self.raise_before = self.call_need - before_call_need

    def cleanup_phase(self):
        self.turn_player_status = Status.Waiting
        self.call_need = 0
        self.raise_before = 0

    def cleanup_round(self):
        self.turn_player_status = Status.Waiting
        self.turn = 0
        self.call_need = 0
        self.raise_before = 0
        self.main_pot = 0


#player１人の情報を持つクラス
class Player():
    
    def __init__(self):
        self.name = None
        self.status = Status.Waiting
        self.position = None
        self.betting = 0
        self.cip = 100
        self.log_win = 0
        self.log_join = 0
        self.log_raise = 0
        self.log_allin = 0
        self.personal_bet = 0
        #各ラウンドでいくら賭けたか　ラウンドが変わるとリセットされる
        self.log_bet = []
        #各ラウンドでのcipの推移　ゲームが終わるまで保持される
        self.log_cip = []
        self.log_cip.append(self.cip)
    
    #名前を設定する
    def set_name(self, name):
        self.name = name

    #blindについての設定をする
    def set_blind(self, sb_value):
        self.status = Status.Blind
        self.betting = sb_value
        self.personal_bet = sb_value
        self.cip -= self.betting


    #ポジションを設定する
    def set_position(self, name):
        self.position = name

    #callを行った場合の処理
    def do_call(self, call_need):
        self.status = Status.Called
        tmp_box = call_need - self.betting
        self.betting += tmp_box
        self.personal_bet += tmp_box
        self.cip -= tmp_box

    #raiseを行った場合の処理
    def do_raise(self, value):
        self.status = Status.Raised
        self.log_raise += 1
        self.betting += value
        self.personal_bet += value
        self.cip -= value

    #checkを行った場合の処理
    def do_check(self):
        self.status = Status.Cheched

    #foldを行った場合の処理
    def do_Fold(self):
        self.status = Status.Folded

    #allinを行った場合の処理
    def do_allin(self):
        self.status = Status.Allin
        self.betting += self.cip
        self.personal_bet += self.cip
        self.log_allin += 1
        self.cip = 0

    #命令を判断する
    def judge_command(self, command, call_need):
        if type(command) == int:
            self.do_raise(command)
        elif command == 'c':
            self.do_call(call_need)
        elif command == 't':
            self.do_check()
        elif command == 'f':
            self.do_Fold()
        elif command == 'allin':
            self.do_allin()
        else:
            print("error do_command")
            
    #フロップに参加した場合を記録する
    def record_join(self):
        self.log_join += 1

    #現在まで賭けた金額を出力する
    def export_bet(self):
        sum = 0
        for i in range(len(self.log_bet)):
            sum += self.log_bet[i]
        if self.betting != -1:
            sum += self.betting 
        return sum
            
    #勝った時の処理
    def win(self, sum):
        self.log_win += 1
        self.cip += sum        
    
    #１つのフェイズが終了した際に必要な処理
    def cleanup_phase(self):
        if self.status == Status.Folded or self.status == Status.Allin:
            self.action = Action.taken
        else:
            self.status = Status.Waiting
        self.log_bet.append(self.betting)
        self.betting = 0
            

    #１つのラウンドが終了した際に必要な処理
    def cleanup_round(self):
        self.log_cip.append(self.cip)
        self.status = Status.Waiting
        self.action = Action.Stand
        self.personal_bet = 0
        self.log_bet = []
        self.betting = 0