from typing import List

from sympy import N
import InFunc
import infor

def players_data()-> List[infor.Player]:
    """プレイヤーデータを外部からの入力を元に作成

    Returns:
        players
    """

    print("Set up the players.")

    #参加者の人数を入力する
    print("Enter the number of players.")

    players_number = InFunc.between2and6()

    players = []
    for i in range(players_number):
        players.append(infor.Player())

    print("The number entered is ",players_number)
    print("")

    #参加者の名前を入力する
    print("Enter the name of the person.")
    for i in range(players_number):
        players[i].set_name(input())

    print("Players setup is finished.")
    print("")

    return players


def setting_data(players:List[infor.Player])-> infor.Setting:
    """設定を外部からの入力を元に作成

    Args:
        players (List[infor.Player]): 

    Returns:
        infor.Setting: 
    """
    
    print("Set up the game.")
    print("Enter the amount for small blind.")

    setting = infor.Setting()
    setting.set_sb_value(InFunc.int_data())

    print("Small blind is ", setting.sb_value)

    print("Enter the initial cip.")

    tmp_box = InFunc.int_data()
    for i in range(len(players)):
        players[i].set_cip(tmp_box)

    print("Initial cip is ", tmp_box)
    print("Game setup is finished.")
    print("")

    return setting


def add_cip(players:List[infor.Player])->List[infor.Player]:
    """チップの追加を設定

    Args:
        players (List[infor.Player]): 

    Returns:
        List[infor.Player]: 
    """

    print("Set up the player's cip.")

    Redo_Flag = True
    while(Redo_Flag):
        print("Enter the number of player which you want to add the cip.")

        for i in range(len(players)):
            print(players[i].name, "is", i)

        numbet_select = InFunc.selected_player(players)

        print("How much do you want to add cip?")

        cip_addtional = InFunc.int_data()

        players[numbet_select].set_cip(players[numbet_select].cip+cip_addtional)

        print(players[numbet_select].name," added ",cip_addtional,"$.")
        print("You have ",players[numbet_select].cip,"$.")

        print("Enter C to continue or Q to stop.")
        entered_char = InFunc.cq_data()
        if entered_char == "q":
            Redo_Flag = False

    print("Cip setup is finished.")
    print("")

    
    return players