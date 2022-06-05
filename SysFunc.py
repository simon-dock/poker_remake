from distutils.log import info
from itertools import count
from re import I
import PhaseFunc
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
    fold_count = 0
    while(End_Flag):

        #プリフロップ
        PhaseFunc.preflop(players, setting)
        

        fold_count = com.count_fold(cip_data, cip_index, players_number)
        if fold_count < players_number-1:
            #フロップ
            cip_data, cip_index = add_mana.process_flop(cip_data, cip_index, name_data, players_number, dealer, sb_player)

        fold_count = com.count_fold(cip_data, cip_index, players_number)
        if fold_count < players_number-1:
            #ターン
            cip_data, cip_index = add_mana.process_turn(cip_data, cip_index, name_data, players_number, dealer, sb_player)

        fold_count = com.count_fold(cip_data, cip_index, players_number)
        if fold_count < players_number-1:
            #リバー
            cip_data, cip_index = add_mana.process_river(cip_data, cip_index, name_data, players_number, dealer, sb_player)
            
        fold_count = com.count_fold(cip_data, cip_index, players_number)
        if fold_count < players_number-1:
            #ショウダウン
            cip_data, cip_index = add_mana.process_showdwon(cip_data, cip_index, name_data, players_number)
        else:
            #最後まで降りなかった人が勝つ処理
            cip_data, cip_index = add_mana.process_survive(cip_data, cip_index, name_data, players_number)
        
        print("Enter C to continue or Q to stop.")
        entered_char = com.check_data_qc()

        if entered_char == "q":
            End_Flag = False

        dealer = com.process_next_dealer(dealer, players_number)

    print("--------------------")
    print("GAME OVER")