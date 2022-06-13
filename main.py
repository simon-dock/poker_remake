import DisFunc
import MakeFunc
import SysFunc
import WriteFunc
import infor
import pyfor

import pygame as pg
import sys
from pygame.locals import *

pystatus = pyfor.Status

#ウィンドウの初期化
pg.init()

WIN = pg.display.set_mode((pyfor.WIN_WIDTH, pyfor.WIN_HEIGHT))

pg.display.set_caption("Poker_Tool")

def jud_key(key: int):
    """
    入力されたキーに対応する文字を返す関数
    扱えないキーが入力された場合はNoneを返す
    Pygameのキーは定数(整数)が割り当てられているので引数はint型になる
    扱える文字は以下の通り
    ・アルファベット(A-Z, a-z)
    ・数字(0-9)
    ・半角スペース
    """
    if (key >= pg.K_a)and(key <= pg.K_z):  # アルファベットが入力された？
        if pg.key.get_mods() & pg.KMOD_SHIFT:  # Shiftキーが入力された？
            return pg.key.name(key).upper()  # 大文字
        else:
            return pg.key.name(key)  # 小文字
    elif ((key >= pg.K_0)and(key <= pg.K_9)):  # 0-9が入力された？
        if pg.key.get_mods() & pg.KMOD_SHIFT:  # Shiftキーが入力された？
            return None
        else:
            return pg.key.name(key)
    elif key == pg.K_SPACE:  # スペースが入力された？
        return ' '
    else:  # 例外？
        return None


def main():

    run = True
    pyset = pyfor.Setting()

    template = pg.font.SysFont(None,100)

    # テキスト入力処理の初期設定

    txt = template.render('|', True, pyfor.WHITE)  # カーソルだけを表示

    txt_give = ''  # 確定(Enter)された文字列を保持する変数
    txt_words = []  # 入力された文字を保持するリスト
    txt_tmp = ''  
    players = []

    while run:
        pg.time.delay(30)
        
        for event in pg.event.get():
            WIN.fill(pyfor.BLACK)
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.KEYDOWN:  # キー入力検知？
                if event.key == pg.K_RETURN:  # Enter押下？
                    txt_give = ''.join(txt_words)  # 文字列に直して保持
                    txt_words = []  # 初期化
                    txt_tmp = ''  # 初期化
                    print('input \'Enter\'')  # ログ
                    pyset.set_entered(True)
                    pyset.set_txt(txt_give)
                elif event.key == pg.K_BACKSPACE:  # BackSpace押下？
                    if not len(txt_words) == 0:  # 入力中の文字が存在するか？
                        txt_words.pop()  # 最後の文字を取り出す(削除)
                else:  # 上記以外のキーが押された時
                    txt_tmp = jud_key(event.key)
                    if not txt_tmp == None:  # 入力可能な文字？
                        txt_words.append(txt_tmp)  #

                if len(txt_words) != 0:  # 入力中のテキストがあるか？
                    txt = template.render(''.join(txt_words) + '|', True, pyfor.WHITE)  # テキストとカーソルを表示
                else:
                    txt = template.render('|', True, pyfor.WHITE)  # カーソルだけを表示

                # テキストの描画(表示物, (x座標, y座標))

            #プログラムの起動メッセージ
            if pyset.status_func == pystatus.Initial:
                pyset = DisFunc.massege_start(WIN,pyset) 

            #参加者のデータリストを作成
            if pyset.status_func == pystatus.MakeFunc:
                players, pyset= MakeFunc.players_data(WIN,players,pyset)

            #ゲームの設定を行う
            #setting = MakeFunc.setting_data(players)

            #ポーカーの管理をする
            #players = SysFunc.poker(players, setting)

            #結果を表示する
            #DisFunc.result(players)

            #結果をテキストファイルに出力する
            #WriteFunc.result(players)

        WIN.blit(txt, (pyfor.WIN_WIDTH/12,pyfor.WIN_HEIGHT*3/4))
        pg.display.update()

if __name__ == '__main__':
    main()