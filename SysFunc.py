from cmath import inf
from typing import List
import PhaseFunc
import MakeFunc
import InFunc
import GetFunc
import infor
import random

def initial_position(players:List[infor.Player])->List[infor.Player]:
    """dealerbuttonを決め、初期ポジションを決定する

    Args:
        players (List[infor.Player]): 

    Returns:
        List[infor.Player]: 
    """
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

    return players


def end_or_finish(Redo_Flag:bool)->bool:
    """ゲームを終了するか続けるかを処理する

    Args:
        Redo_Flag (bool): 

    Returns:
        bool: 
    """
    print("If you want to quit the game, enter y/n.")
    entered_char = InFunc.yn_data()
    if entered_char == "y":
        Redo_Flag = False

    return Redo_Flag


def cleanup_cip(players:List[infor.Player])->List[infor.Player]:
    """ラウンドの終わりにcipが0にならないように処理をする

    Args:
        players (List[infor.Player]): 

    Returns:
        infor.Player: 
    """
    ZeroCip_Flag = True
    AddCip_Flag = False
    while(ZeroCip_Flag):
        if GetFunc.zero_cip_count(players) == 0:
            ZeroCip_Flag = False

        if ZeroCip_Flag == True:
            AddCip_Flag = True
            print("If you have 0 cip, please add cip.")
            players = MakeFunc.add_cip(players)

    if AddCip_Flag == False:
        print("If you want to add a cip, enter y/n.")
        entered_char = InFunc.yn_data()
        if entered_char == "y":
            players = MakeFunc.add_cip(players)
        
    return players



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

    players = initial_position(players)

    Redo_Flag = True
    phase_name = ['Flop', 'Turn', 'River']

    while(Redo_Flag):
        players, setting = PhaseFunc.preflop(players, setting)
        for i in range(len(phase_name)):
            players, setting = PhaseFunc.common(players, setting, phase_name[i])
        players, setting = PhaseFunc.showdwon_or_autowin(players, setting)
        Redo_Flag = end_or_finish(Redo_Flag)
        if Redo_Flag == True:
            players = cleanup_cip(players)

        
    print("#####################")
    print("GAME OVER")
    print("")

    return players
