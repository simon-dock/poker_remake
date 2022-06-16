import matplotlib.pyplot as plt

#プログラムの起動メッセージ
def massege_start():
    print("#####################")
    print("")
    print("start Tool of Poker")
    print("")
    print("#####################")
    print("")

#結果を表示
def result(players, setting):

    print("#####################")
    print("RESULT")
    print("")

    game_count = len(players[0].log_cip)-1
    print("Count of game", game_count)
    
    for i in range(len(players)):
        print(players[i].name)
        print("Cip is $",players[i].cip)
        print("Number of wins is               ",players[i].log_win,", ",100*(players[i].log_win/game_count),"%")
        print("Number of players on the flop is",players[i].log_join,", ",100*(players[i].log_join/game_count),"%")
        print("Number of raise is              ",players[i].log_raise)
        print("Number of alli-in is            ",players[i].log_allin)
        plt.plot(players[i].log_cip, label = players[i].name)
        print("")

    plt.grid()
    plt.legend()
    plt.show()