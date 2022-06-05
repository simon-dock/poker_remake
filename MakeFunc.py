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

    #参加者の名前を入力する　左隣の人の名前を入力していく
    for i in range(players_number):
        if i == 0:
            print("Enter the name of the first person.")
        else:
            print("Eenter the name of the person to your left.")
        players[i].set_name(input())

    print("Players setup is finished.")
    print("")