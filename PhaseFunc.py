import ComFunc
import InFunc
import infor

status = infor.status
position = infor.Position

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

    while(1):
        
        #フォールドしていなければ
        if players[now_player].status != status.Folded:

            #データの表示
            print("Now    Player is ",players[now_player].name)
            print("You are betting $",players[now_player].betting)
            print("Max bet is $",max_bet)
            
            #入力受付、格納
            no = InFunc.what_do()
            

        print(now_bet)
        cip_data[cip_index][com.cast_cip(now_player)] = now_bet
        
        return now_bet