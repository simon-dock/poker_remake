from typing import List
import InFunc
import infor
import copy

status = infor.Status
position = infor.Position


def next_index(players:List[infor.Player] , now_index:int)-> int:
    """次の添字を取得

    Args:
        players (List[infor.Player]): 
        now_index (int): 

    Returns:
        int: 
    """

    next_index = now_index + 1
    if next_index == len(players):
        next_index = 0

    return next_index


def status_count(players:List[infor.Player] , status:infor.Status)-> int:
    """特定の状態の人の数を取得

    Args:
        players (List[infor.Player]): 
        status (str): 

    Returns:
        int: 
    """
    count = 0
    for i in range(len(players)):
        if players[i].status == status:
            count += 1
    return count


def zero_cip_count(players:List[infor.Player])-> int:
    """cipが0の人の数を取得

    Args:
        players (List[infor.Player]): 

    Returns:
        int: 
    """
    count = 0
    for i in range(len(players)):
        if players[i].cip == 0:
            count += 1
    return count


def remain_count(Redo_Flag:bool, players:List[infor.Player])-> bool:
    """何人残っているかを判断しフラグの状態を取得

    Args:
        Redo_Flag (bool): 
        players (List[infor.Player]): 

    Returns:
        bool: 
    """
    fold_count = status_count(players, status.Folded)
    if fold_count == len(players)-1:
        Redo_Flag = False

    return Redo_Flag

def check_comfirm(Redo_Flag, players, setting, backup_play, backup_set):
    print("If you want to back, enter y/n.")
    enteredchar = InFunc.yn_data()
    if enteredchar == 'y':
        print("")
        print("--------------------")
        print("Roll Back 1 phase")
        print("--------------------")
        print("")
        players = copy.deepcopy(backup_play)
        setting = copy.deepcopy(backup_set)
        Redo_Flag = True
    
    return Redo_Flag, players, setting, backup_play, backup_set