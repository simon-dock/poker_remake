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
            #potの計算
            sum = 0
            for i in range(len(players)):
                sum += players[i].export_bet()
            setting.reload_main_pot(sum)

            #データの表示
            print("--------------------")
            print("Now Player is ",players[setting.turn].name)
            print("You are betting $",players[setting.turn].betting)
            print("You have        $",players[setting.turn].cip)
            print("Max bet is      $",setting.max_bet)
            print("Pot has         $",setting.main_pot)
            print("--------------------")
            
            #入力受付、格納
            command = InFunc.what_do(players, setting)
            players[setting.turn].judge_command(command, setting.max_bet)

            #場の最大掛け金の更新
            if players[setting.turn].status == status.Raised or players[setting.turn].status == status.Allin:
                setting.reload_max_bet(players[setting.turn].betting)

    #次のプレイヤーの添字を取得
    setting.turn = GetFunc.next_index(players, setting.turn)

    #次のプレイヤーの掛け金が場の掛け金と同額かつ
    #Wating状態でなくtaken状態でもなければ終了
    if players[setting.turn].betting == setting.max_bet:
        if players[setting.turn].status != status.Waiting and players[setting.turn].action != action.taken:
            Redo_Flag = False

    return Redo_Flag, players, setting


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
            setting.turn = GetFunc.next_index(players, i)

    if len(players) == 2:
        players[0].status = status.Blind
        players[0].betting = setting.sb_value*2
        players[i].cip -= players[i].betting
        setting.turn = GetFunc.next_index(players, 0)

    setting.blind()
    Redo_Flag = True
    First_Flag = True

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

    
    #フェイズの後処理    
    return clean_up_phase(players, setting) 


#プリフロップ以外の処理
def common(players, setting, phase_name):

    #Waitingの人数を数える
    waiting_count = GetFunc.status_count(players, status.Waiting)

    #wating状態が一人の場合この処理を飛ばす
    if waiting_count == 1:
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
    fold_list = []
    fold_index = [0 for i in range(len(players))]

    for i in range(len(players)):
        if players[i].status == status.Folded:
            fold_list.append(i)
            fold_index[i] = 1
        if players[i].status == status.Waiting:
            waiting_list.append(i)

    #allin状態がおらずwaiting状態が一人の場合autowinの処理
    if len(players) - len(fold_list) == 1:
        winner_index = waiting_list[0]
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
