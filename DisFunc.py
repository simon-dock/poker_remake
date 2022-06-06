import numpy as np
import random

#プログラムの起動メッセージ
def massege_start():
    print("#####################")
    print("")
    print("start Tool of Poker")
    print("")
    print("#####################")
    print("")

#結果を表示
def result(players):

    print("#####################")
    print("RESULT")
    print("")
    
    for i in range(len(players)):
        print(players[i].name)
        print("Chip is $",players[i].cip)
        print("Number of wins is               ",players[i].log_win)
        print("Number of players on the flop is",players[i].log_join)
        print("Number of raise is              ",players[i].log_raise)
        print("Number of alli-in is            ",players[i].log_allin)
        print(players[i].log_cip)
        print("")