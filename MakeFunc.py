import ComFunc

#プレイヤーデータを作成
def players_data():
    print("Set up the players.")

    Redo_Flag = True
    while(Redo_Flag):
        print("Enter the number of players.")

        players_number = add_play.input_players_number()

        name_data = add_play.input_players_name(players_number)

        Redo_Flag = add_play.confirm_players(name_data)

        if Redo_Flag == True:
            print("Redo the players settings.")

    print("Players setup is finished.")
    print("")