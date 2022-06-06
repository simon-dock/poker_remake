from distutils.log import info
from itertools import count
from re import I
import PhaseFunc
import InFunc
import infor
import random

def poker(players, setting):
    
    print("--------------------")
    print("GAME START")

    #dealerbuttonを決め、初期ポジションを決定する
    random.shuffle(players)
    times = 0
    for i in infor.Position:
        if times == len(players):
            break
        players[times].position = i
        print(players[times].name,players[times].position)
        times += 1


    End_Flag = True
    phase_name = ['Flop', 'Turn', 'River']
    while(End_Flag):

        #プリフロップ
        players, setting = PhaseFunc.preflop(players, setting)

        #フロップ、ターン、リバー
        for i in range(len(phase_name)):
            players, setting = PhaseFunc.common(players, setting, phase_name[i])

        #ショウダウン
        players, setting = PhaseFunc.showdwon_or_autowin(players, setting)
        
        print("Enter C to continue or Q to stop.")
        entered_char = InFunc.cq_data()

        if entered_char == "q":
            End_Flag = False

        #ポジションを回す
        tmp_position = players[0].position
        for i in range(len(players)-1):
            players[i].position = players[i+1].position
        players[len(players)-1].position = tmp_position

    print("--------------------")
    print("GAME OVER")

    return players