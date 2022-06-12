from typing import List
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


#設定を作成
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