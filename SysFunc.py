from typing import List
import PhaseFunc
import InFunc
import infor
import random

def poker(players: List[infor.Player], setting: infor.Setting)-> List[infor.Player]:
    """ポーカーの処理を行う

    Args:
        players (List[infor.Player]): 
        setting (infor.Setting): 

    Returns:
        List[infor.Player]:
    """
    print("#####################")
    print("GAME START")
    print("")

    #dealerbuttonを決め、初期ポジションを決定する
    random.shuffle(players)
    times = 0
    print("--------------------")
    for i in infor.Position:
        if times == len(players):
            break
        players[times].set_position(i)
        print(players[times].name,players[times].position.name)
        times += 1
    print("--------------------")
    print("")

    End_Flag = True
    phase_name = ['Flop', 'Turn', 'River']
    while(End_Flag):
        players, setting = PhaseFunc.preflop(players, setting)
        for i in range(len(phase_name)):
            players, setting = PhaseFunc.common(players, setting, phase_name[i])
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

    print("#####################")
    print("GAME OVER")
    print("")

    return players