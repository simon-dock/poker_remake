import pyfor

import pygame as pg
from pygame.locals import *

#プログラムの起動メッセージ
def massege_start(WIN, pyset):
    template = pg.font.SysFont(None,300)
    text = template.render("Tool of Poker", True, pyfor.WHITE)
    WIN.blit(text, (pyfor.WIN_WIDTH/12,pyfor.WIN_HEIGHT/3))
    pg.display.update()
    pg.time.delay(2000)
    WIN.fill(pyfor.BLACK)

    pyset.set_status_func(pyfor.Status.MakeFunc)

    return pyset

#結果を表示
def result(players):

    print("#####################")
    print("RESULT")
    print("")
    
    for i in range(len(players)):
        print(players[i].name)
        print("Chip is $",players[i].cip)
        print("Number of wins is               ",players[i].log_win)
        print("Number of players on the flop is",players[i].log_join)
        print("Number of raise is              ",players[i].log_raise)
        print("Number of alli-in is            ",players[i].log_allin)
        print(players[i].log_cip)
        print("")