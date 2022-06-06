from itertools import count
from operator import setitem
import GetFunc
import InFunc
import infor

status = infor.Status
action = infor.Action
position = infor.Position

#通常のフェイズの処理
def run_poker(Redo_Flag, players, setting):

    #フォールド,オールインしていない且つ
    # standであれば
    if players[setting.turn].status != status.Folded and players[setting.turn].status != status.Allin:
        if players[setting.turn].action == action.Stand:

            #データの表示
            print("--------------------")
            print("Now Player is ",players[setting.turn].name)
            print("You have         $",players[setting.turn].cip)
            print("Pot has          $",setting.main_pot)
            if len(setting.side_pot) >= 1:
                for i in range(len(setting.side_pot)):
                    if setting.side_pot[i] != setting.main_pot:
                        print(players[setting.side_pot_whose[i]].name," pot ","is $",setting.side_pot[i])
            print("You are betting  $",players[setting.turn].betting)
            print("Max bet is       $",setting.call_need)
            print("Minimum raise is $",setting.call_need+setting.raise_before)
            print("--------------------")
            
            #入力受付、格納
            command = InFunc.what_do(players, setting)
            players[setting.turn].judge_command(command, setting.call_need)
            setting.reload_turn_player_status(players[setting.turn].status)

            #場の最大掛け金の更新 raiseの場合
            if players[setting.turn].status == status.Raised:
                before_call_need = setting.call_need
                setting.reload_call_need(players[setting.turn].betting)
                setting.raise_before = setting.call_need - before_call_need

            #allinの場合
            if players[setting.turn].status == status.Allin:
                if players[setting.turn].betting > setting.call_need:
                    before_call_need = setting.call_need
                    setting.reload_call_need(players[setting.turn].betting)
                    setting.raise_before = setting.call_need - before_call_need

            #potの計算
            players, setting = get_pot(players, setting)

    #次のプレイヤーの添字を取得
    setting.turn = GetFunc.next_index(players, setting.turn)

    #次のプレイヤーの掛け金が場の掛け金と同額かつ
    #Wating状態でなくtaken状態でもなければ終了
    if players[setting.turn].betting == setting.call_need:
        if players[setting.turn].status != status.Waiting and players[setting.turn].action != action.taken:
            Redo_Flag = False
        taken_count = GetFunc.action_count(players, action.taken)
        if taken_count == len(players):
            Redo_Flag = False

    return Redo_Flag, players, setting


#potを計算する
def get_pot(players, setting):

    if len(setting.side_pot) != 0:
        for i in range(len(setting.side_pot)): 
            setting.reload_side_pot(sum_betting(players),i)
        
    if setting.turn_player_status == status.Allin:
        setting.make_side_pot(sum_betting(players), setting.turn)
 
    setting.reload_main_pot(sum_betting(players))

    return players, setting

def sum_betting(players):
    sum = 0
    for i in range(len(players)):
        sum += players[i].export_bet()

    return sum

#フェイズの後処理
def clean_up_phase(players, setting):
    setting.cleanup_phase()
    for i in range(len(players)):
        players[i].cleanup_phase()
    return players, setting

#ラウンドの後処理
def clean_up_round(players, setting):
    setting.cleanup_round()
    for i in range(len(players)):
        players[i].cleanup_round()
    return players, setting

#preflopの処理
def preflop(players, setting):

    print("/////////////////")
    print("Now it's Preflop.")
    print("/////////////////")
    print("")

    #sb,bbの状態とベットを設定し、次のプレイヤーの添字を入手する
    for i in range(len(players)):
        if players[i].position == position.SmallBlind:
            players[i].status = status.Blind
            players[i].betting = setting.sb_value
            players[i].cip -= players[i].betting

        if players[i].position == position.BigBlind:
            players[i].status = status.Blind
            players[i].betting = setting.sb_value*2
            players[i].cip -= players[i].betting
            setting.raise_before = players[i].betting
            setting.turn = GetFunc.next_index(players, i)

    if len(players) == 2:
        players[0].status = status.Blind
        players[0].betting = setting.sb_value*2
        players[i].cip -= players[i].betting
        setting.raise_before = players[i].betting
        setting.turn = GetFunc.next_index(players, 0)

    setting.blind()
    Redo_Flag = True
    First_Flag = True

    #potの計算
    players, setting = get_pot(players, setting)

    while(Redo_Flag):
        
        Redo_Flag, players, setting = run_poker(Redo_Flag, players, setting)

        #一度もレイズされずbbに回った場合レイズする権利がある
        if players[setting.turn].betting == setting.sb_value*2 and First_Flag == True:
            #何人残っているか確認する
            fold_count = GetFunc.status_count(players, status.Folded)
            if fold_count != len(players)-1:
                if players[setting.turn].position == position.BigBlind:
                    Redo_Flag = True
                    First_Flag = False

    #フロップに参加した人への処理
    for i in range(len(players)):
        if players[i].status != status.Folded:
            players[i].record_join()

    #フェイズの後処理    
    return clean_up_phase(players, setting) 


#プリフロップ以外の処理
def common(players, setting, phase_name):

    #Waitingとtakenの人数を数える
    waiting_count = GetFunc.status_count(players, status.Waiting)
    taken_count = GetFunc.action_count(players, action.taken)

    #wating状態が一人の場合この処理を飛ばす
    if waiting_count == 1 or taken_count == len(players):
        return players, setting
            
    print("/////////////////")
    print("Now it's",phase_name)
    print("/////////////////")
    print("")

    #Smallblindからはじまる
    for i in range(len(players)):
        if players[i].position == position.SmallBlind:
            setting.turn = i

    Redo_Flag = True

    while(Redo_Flag):
        Redo_Flag, players, setting = run_poker(Redo_Flag, players, setting)

    return  clean_up_phase(players, setting) 



def showdwon_or_autowin(players, setting):
    #foldの人数を数える
    waiting_list = []
    allin_list = []
    fold_list = []
    fold_index = [0 for i in range(len(players))]

    for i in range(len(players)):
        if players[i].status == status.Folded:
            fold_list.append(i)
            fold_index[i] = 1
        if players[i].status == status.Allin:
            allin_list.append(i)
        if players[i].status == status.Waiting:
            waiting_list.append(i)

    #allin状態かwaiting状態が一人の場合autowinの処理
    if len(players) - len(fold_list) == 1:
        if len(waiting_list) == 1:
            winner_index = waiting_list[0]
        if len(allin_list) == 1:
            winner_index = allin_list[0]
        print("Winnner is",players[winner_index].name)
        print("Get pot $",setting.main_pot)
        players[winner_index].win(setting.main_pot)
        
    #そうでない場合、showdownを行う
    else:
        for i in range(len(players)):
            if fold_index[i] == 0:
                print(players[i].name," is ", i)
        
        print("Who won?")
        winner_index = InFunc.winner(fold_index)
        print("Winnner is",players[winner_index].name)
        print("Get pot $",setting.main_pot)
        players[winner_index].win(setting.main_pot)

    return clean_up_round(players, setting)
