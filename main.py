import DisFunc
import MakeFunc
import infor

def main():

    #プログラムの起動メッセージ
    DisFunc.massege_start() 

    #参加者のデータリストを作成
    MakeFunc.players_data()

    #ゲームの設定を行う
    #sb_value = funcs.make_game_setting()

    #ポーカーの管理をする
    #cip_data, cip_index = funcs.manage_poker(name_data, sb_value)

    #戦績を精算
    #calculate_result(cip_data, cip_index, name_data)

    #結果を表示する
    # display_result()

    #結果をテキストファイルに出力する
    # export_result()

if __name__ == '__main__':
    main()