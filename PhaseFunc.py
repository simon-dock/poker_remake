import ComFunc
import InFunc
import infor

status = infor.Status
position = infor.Position

#通常のフェイズの処理
def run_poker(Redo_Flag, players, now_player, max_bet):

    #フォールドしていなければ
    if players[now_player].status != status.Folded:

        #データの表示
        print("Now    Player is ",players[now_player].name)
        print("You are betting $",players[now_player].betting)
        print("Max bet is $",max_bet)
        
        #入力受付、格納
        command = InFunc.what_do(players, now_player, max_bet)
        players[now_player].judge_command(command, max_bet)

    #場の最大掛け金の更新
    if players[now_player].status == status.Raised:
        max_bet = players[now_player].betting

    #次のプレイヤーの添字を取得
    now_player = ComFunc.get_next_index(players, now_player)

    #次のプレイヤーの掛け金が場の掛け金と同額なら終了
    if players[now_player].betting == max_bet:
        Redo_Flag = False

    return Redo_Flag, players, now_player, max_bet


#preflopの処理
def preflop(players, setting):

    print("--------------------")
    print("Now it's Preflop.")
    print("")

    #sb,bbの状態とベットを設定し、次のプレイヤーの添字を入手する
    for i in range(len(players)):
        if players[i].position == position.SmallBlind:
            players[i].status = status.Blind
            players[i].betting = setting.sb_value

        if players[i].position == position.BigBlind:
            players[i].status = status.Blind
            players[i].betting = setting.sb_value*2
            now_player = ComFunc.get_next_index(players, i)

    if len(players) == 2:
        players[0].status = status.Blind
        players[0].betting = setting.sb_value*2
        now_player = ComFunc.get_next_index(players, 0)

    max_bet = setting.sb_value*2
    Redo_Flag = True

    while(Redo_Flag):
        
        Redo_Flag, players, now_player, max_bet = run_poker(Redo_Flag, players, now_player, max_bet)

        #一度もレイズされずbbに回った場合レイズする権利がある
        if players[now_player].betting == setting.sb_value*2:
            if players[now_player].position == position.BigBlind:
                Redo_Flag = True