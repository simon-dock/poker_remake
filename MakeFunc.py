from typing import List
from numpy import Inf

from sympy import N
import pygame as pg
import InFunc
import infor
import pyfor

pystatus = pyfor.Status

def players_data(WIN,players,pyset):
    """プレイヤーデータを外部からの入力を元に作成

    Returns:
        players
    """

    WIN.fill(pyfor.BLACK)
    template = pg.font.SysFont(None,100)

    #参加人数を入力する
    if pyset.status_inner == pystatus.Initial:
        text = template.render("Set up the players.", True, pyfor.WHITE)
        WIN.blit(text, (pyfor.WIN_WIDTH/12,pyfor.WIN_HEIGHT/4))
        text = template.render("Enter the number of players.", True, pyfor.WHITE)
        WIN.blit(text, (pyfor.WIN_WIDTH/12,pyfor.WIN_HEIGHT/4+100))

        #入力があった時
        if pyset.entered == True:
            Correct_Flag, value = InFunc.between2and6(pyset.txt)
            WIN.fill(pyfor.BLACK)

            if Correct_Flag == True:
                players_number = value
                for i in range(players_number):
                    players.append(infor.Player())
                pyset.set_status_inner(pystatus.MakeP_1)
                pyset.set_entered(False)
            else:
                text = template.render("Please enter the number 2~6.", True, pyfor.WHITE)
                WIN.blit(text, (pyfor.WIN_WIDTH/12,pyfor.WIN_HEIGHT/4))

        #参加者の名前を入力する
        if pyset.status_inner == pystatus.MakeP_1:
            text = template.render("Enter the name of the person.", True, pyfor.WHITE)
            WIN.blit(text, (pyfor.WIN_WIDTH/12,pyfor.WIN_HEIGHT/4))
            print("w")

            #入力があった時
            if pyset.entered == True:
                Correct_Flag, value = InFunc.between2and6(pyset.txt)
                WIN.fill(pyfor.BLACK)

                if Correct_Flag == True:
                    players_number = value
                    for i in range(players_number):
                        players.append(infor.Player())
                    pyset.set_status_inner(pystatus.MakeP_1)
                    pyset.set_entered(False)
                    text = template.render("The number entered is "+"".join(str(players_number)), True, pyfor.WHITE)
                    WIN.blit(text, (pyfor.WIN_WIDTH/12,pyfor.WIN_HEIGHT/4))

                else:
                    text = template.render("Please enter the number 2~6.", True, pyfor.WHITE)
                    WIN.blit(text, (pyfor.WIN_WIDTH/12,pyfor.WIN_HEIGHT/4))

    #print()
    #print("")

    #参加者の名前を入力する
    #print("")
    #for i in range(players_number):
    #    players[i].set_name(input())

    #print("Players setup is finished.")
    #print("")

    return players, pyset


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