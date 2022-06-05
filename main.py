import DisFunc
import MakeFunc
import SysFunc
import infor

def main():

    #プログラムの起動メッセージ
    DisFunc.massege_start() 

    #参加者のデータリストを作成
    players = MakeFunc.players_data()

    #ゲームの設定を行う
    setting = MakeFunc.setting_data()

    #ポーカーの管理をする
    SysFunc.poker(players, setting)

    #戦績を精算
    #calculate_result(cip_data, cip_index, name_data)

    #結果を表示する
    # display_result()

    #結果をテキストファイルに出力する
    # export_result()

if __name__ == '__main__':
    main()