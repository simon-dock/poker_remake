from enum import Enum

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
        self.first_bb = True
        self.turn_player_status = Status.Waiting
        self.call_need = 0
        self.raise_before = 0
        self.main_pot = 0
        self.most_cip_ever = 100

    #betの最小単位を設定
    def set_sb_value(self, value):
        self.sb_value = value

    #現在のプレイヤーの添字を設定
    def set_turn(self, turn):
        self.turn = turn

    #ファーストフラグを設定
    def set_first_bb(self, status):
        self.first_bb = status

    #過去一番多いチップ所持数を設定
    def set_most_cip_ever(self, value):
        self.most_cip_ever = value

    #現在のプレイヤーの状態を設定
    def set_turn_player_status(self, status):
        self.turn_player_status = status

    #callに必要な額を設定
    def set_call_need(self, new_max):
        self.call_need = new_max

    #前のレイズの差額がいくらか設定
    def set_raise_before(self, value):
        self.raise_before = value

    #メインポットを設定する
    def set_main_pot(self,sum):
        self.main_pot = sum

    #ブラインドの処理
    def update_blind(self, turn):
        self.set_raise_before(self.sb_value*2)
        self.set_call_need(self.raise_before)
        self.set_turn(turn)
        
    #レイズされたときの処理
    def update_raise_before(self, betting):
        before_call_need = self.call_need
        self.set_call_need(betting)
        self.set_raise_before(self.call_need - before_call_need)

    #フェイズの後処理
    def cleanup_phase(self):
        self.set_turn_player_status(Status.Waiting)
        self.set_call_need(0)
        self.set_raise_before(0)

    #ラウンドの後処理
    def cleanup_round(self):
        self.set_turn_player_status(Status.Waiting)
        self.set_first_bb(True)
        self.set_turn(0)
        self.set_call_need(0)
        self.set_raise_before(0)
        self.set_main_pot(0)


#player１人の情報を持つクラス
class Player():
    
    def __init__(self):
        self.name = None
        self.status = Status.Waiting
        self.position = None
        self.betting = 0
        self.cip = 0
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

    #状態を設定する
    def set_status(self, status):
        self.status = status

    #ポジションを設定する
    def set_position(self, position):
        self.position = position

    #ベットした金額を設定する
    def set_betting(self, betting):
        self.betting = betting

    #個人のベット額を設定する
    def set_personal_bet(self, value):
        self.personal_bet = value

    #持ち金を設定する
    def set_cip(self,value):
        self.cip = value

    #log_raiseのカウントを増やす
    def add_log_raise(self):
        self.log_raise += 1
    
    #log_allinのカウントを増やす
    def add_log_allin(self):
        self.log_allin += 1
    
    #log_joinのカウントを増やす
    def add_log_join(self):
        self.log_join += 1

    #log_winのカウントを増やす
    def add_log_win(self):
        self.log_win += 1

    #blindについての設定をする
    def set_blind(self, sb_value):
        self.set_status(Status.Blind)
        self.set_betting(sb_value)
        self.set_personal_bet(sb_value)
        self.set_cip(self.cip-self.betting)


    #callを行った場合の処理
    def do_call(self, call_need):
        self.set_status(Status.Called)
        tmp_box = call_need - self.betting
        self.set_betting(self.betting+tmp_box)
        self.set_personal_bet(self.personal_bet+tmp_box)
        self.set_cip(self.cip-tmp_box)

    #raiseを行った場合の処理
    def do_raise(self, value):
        self.set_status(Status.Raised)
        self.add_log_raise()
        self.set_betting(self.betting+value)
        self.set_personal_bet(self.personal_bet+value)
        self.set_cip(self.cip-value)

    #checkを行った場合の処理
    def do_check(self):
        self.set_status(Status.Cheched)

    #foldを行った場合の処理
    def do_Fold(self):
        self.set_status(Status.Folded)

    #allinを行った場合の処理
    def do_allin(self):
        self.set_status(Status.Allin)
        self.set_betting(self.betting+self.cip)
        self.set_personal_bet(self.personal_bet+self.cip)
        self.add_log_allin()
        self.set_cip(0)

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
        self.add_log_win()
        self.set_cip(self.cip+sum)        
    
    #１つのフェイズが終了した際に必要な処理
    def cleanup_phase(self):
        if self.status == Status.Folded or self.status == Status.Allin:
            pass            
        else:
            self.set_status(Status.Waiting)
        self.log_bet.append(self.betting)
        self.set_betting(0)
            

    #１つのラウンドが終了した際に必要な処理
    def cleanup_round(self):
        self.log_cip.append(self.cip)
        self.set_status(Status.Waiting)
        self.set_betting(0)
        self.set_personal_bet(0)
        self.log_bet = []
        