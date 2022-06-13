
from typing import List
import infor


def int_data()-> int:
    """入力されたデータがint型かチェックする

    Returns:
        int: 
    """
    
    Correct_Flag = True

    while(Correct_Flag):

        tmp_box = input()

        if tmp_box.isnumeric():
            value_int = int(tmp_box)
            Correct_Flag = False
        else:
            print("Please enter the number.")

    return value_int


def cq_data()-> str:
    """入力された文字がq,c判断する

    Returns:
        str:
    """

    Correct_Flag = True

    while(Correct_Flag):

        tmp_box = input()

        if tmp_box == 'q':
            value = 'q'
            Correct_Flag = False
        elif tmp_box == 'c':
            value = 'c'
            Correct_Flag = False
        else:
            print("Please enter Q of quit or C of contine.")

    return value

def ca_data()-> str:
    """入力された文字がa,c判断する

    Returns:
        str:
    """

    Correct_Flag = True

    while(Correct_Flag):

        tmp_box = input()

        if tmp_box == 'c':
            value = 'c'
            Correct_Flag = False
        elif tmp_box == 'a':
            value = 'a'
            Correct_Flag = False
        else:
            print("Please enter A of add or C of contine.")

    return value


def selected_player(players:List[infor.Player])->int:
    """選ばれるプレイヤーを取得する

    Args:
        players (List[infor.Player]): 

    Returns:
        int: 
    """

    Correct_Flag = True

    while(Correct_Flag):

        tmp_box = input()

        if tmp_box.isnumeric():
            tmp_box = int(tmp_box)
            if tmp_box >= 0  and tmp_box < len(players):
                value = tmp_box
                Correct_Flag = False

        if Correct_Flag == True:
            print("Please enter the number.")

    return value


def between2and6(tmp_box)-> int:
    """入力されたデータがint型で2~6かチェックする

    Returns:
        int: 
    """
    value_int = tmp_box

    Correct_Flag = False
    if tmp_box.isnumeric():
        tmp_box = int(tmp_box)
        if tmp_box > 1 and tmp_box < 7:
            value_int = tmp_box
            Correct_Flag = True

    return Correct_Flag, value_int


def winner(fold_index:List[int])-> int:
    """入力されたデータがfold_indexでないかチェックする

    Args:
        fold_index (List[int]): 

    Returns:
        int: 
    """
    
    Correct_Flag = True

    while(Correct_Flag):

        tmp_box = input()

        if tmp_box.isnumeric():
            tmp_box = int(tmp_box)
            if tmp_box < len(fold_index):
                if fold_index[tmp_box] == 0:
                    value_int = tmp_box
                    Correct_Flag = False
            
        if Correct_Flag == True:
            print("Please enter the number.")

    return value_int


def what_do(players:List[infor.Player], setting:infor.Setting)-> any:
    """入力された文字をチェックする

    Args:
        players (List[infor.Player]): 
        setting (infor.Setting): 

    Returns:
        any: 
    """

    Correct_Flag = True
    now_bet = players[setting.turn].betting

    while(Correct_Flag):

        tmp_box = input()

        if tmp_box.isnumeric():
            value = int(tmp_box)
            if now_bet + value >= setting.call_need + setting.raise_before and value <= players[setting.turn].cip :
                Correct_Flag = False
            else:
                print("Please enter correct number")

        else:
            if tmp_box == 't':
                if now_bet == setting.call_need:
                    value = tmp_box
                    Correct_Flag = False
                else:
                    print("You can not Check")
            elif tmp_box == 'c':
                if now_bet != setting.call_need:
                    value = tmp_box
                    Correct_Flag = False
                else:
                    print("You can not Call")
            elif tmp_box == 'f':
                value = tmp_box
                Correct_Flag = False
            elif tmp_box == 'allin':
                value = tmp_box
                Correct_Flag = False
            else:
                print("Please enter the number or C of call")
                print("or T of check or F of fold or allin.")

    return value