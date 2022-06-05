import ComFunc
import infor

#プレイヤーデータを作成
def players_data():
    print("Set up the players.")

    #参加者の人数を入力する
    print("Enter the number of players.")

    players_number = ComFunc.check_data_int()

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
def setting_data():
    
    print("Set up the game.")
    print("Enter the amount for small blind.")

    setting = infor.Setting()
    setting.sb_value = ComFunc.check_data_int()

    print("Small blind is ", setting.sb_value)
    print("Game setup is finished.")
    print("")

    return setting