import DisFunc
import MakeFunc
import SysFunc
import WriteFunc
import infor

import pygame

#ウィンドウの初期化
pygame.init()
WIN_WIDTH = 1100
WIN_HEIGHT = 1200
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


pygame.display.set_caption("Poker_Tool")

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    
def main():

    #プログラムの起動メッセージ
    DisFunc.massege_start() 

    #参加者のデータリストを作成
    players = MakeFunc.players_data()

    #ゲームの設定を行う
    setting = MakeFunc.setting_data(players)

    #ポーカーの管理をする
    players = SysFunc.poker(players, setting)

    #結果を表示する
    DisFunc.result(players)

    #結果をテキストファイルに出力する
    WriteFunc.result(players)

if __name__ == '__main__':
    main()