import DisFunc
import MakeFunc
import SysFunc
import WriteFunc
import infor

def main():

    #プログラムの起動メッセージ
    DisFunc.massege_start() 

    #参加者のデータリストを作成
    players = MakeFunc.players_data()

    #ゲームの設定を行う
    setting = MakeFunc.setting_data(players)

    #ポーカーの管理をする
    players, setting = SysFunc.poker(players, setting)

    #結果を表示する
    DisFunc.result(players, setting)

    #結果をテキストファイルに出力する
    WriteFunc.result(players)

if __name__ == '__main__':
    main()