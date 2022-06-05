from asyncio import start_unix_server
from cgitb import small
from enum import Enum
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
        self.max_bet = 0
        self.main_pot = 0
        self.side_pot = 0

    def blind(self):
        self.max_bet = self.sb_value*2

    def reload_main_pot(self,sum):
        self.main_pot = sum

    def reload_max_bet(self, new_max):
        self.max_bet = new_max

    def cleanup_phase(self):
        self.max_bet = 0

    def cleanup_round(self):
        self.turn = 0
        self.max_bet = 0
        self.main_pot = 0
        self.side_pot = 0


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
        #各フェイズでいくら賭けたか　ラウンドが変わるとリセットされる
        self.log_bet = []
        #各ラウンドでのcipの推移　ゲームが終わるまで保持される
        self.log_cip = []
        self.log_cip.append(self.cip)
    
    #名前を設定する
    def set_name(self, name):
        self.name = name

    #ポジションを設定する
    def set_position(self, name):
        self.position = name

    #callを行った場合の処理
    def do_call(self, value):
        self.status = Status.Called
        self.betting += value
        self.cip -= value

    #raiseを行った場合の処理
    def do_raise(self, value):
        self.status = Status.Raised
        self.log_raise += 1
        self.betting += value
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
        self.log_allin += 1
        self.cip = 0

    #命令を判断する
    def judge_command(self, command, max_bet):
        if type(command) == int:
            if self.betting + command == max_bet:
                self.do_call(command)
            elif self.betting + command >= max_bet*1.25:
                self.do_raise(command)
        elif command == 'c':
            self.do_check()
        elif command == 'f':
            self.do_Fold()
        elif command == 'allin':
            self.do_allin()
        else:
            print("error do_command")

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
            if self.betting != -1:
                self.log_bet.append(self.betting)
            self.betting = -1
        else:
            self.status = Status.Waiting
            self.log_bet.append(self.betting)
            self.betting = 0

    #１つのラウンドが終了した際に必要な処理
    def cleanup_round(self):
        self.log_cip.append(self.cip)
        self.status = Status.Waiting
        self.betting = 0
        self.log_bet = []