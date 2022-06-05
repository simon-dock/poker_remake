import numpy as np

#入力されたデータがint型かチェックする
def check_data_int():
    
    Correct_Flag = True

    while(Correct_Flag):

        tmp_box = input()

        if tmp_box.isnumeric():
            value_int = int(tmp_box)
            Correct_Flag = False
        else:
            print("Please enter the number.")

    return value_int

#入力された文字がc,f,数字か判断する
def check_data_what():

    Correct_Flag = True

    while(Correct_Flag):

        tmp_box = input()

        if tmp_box.isnumeric():
            value_int = int(tmp_box)
            Correct_Flag = False
        elif tmp_box == 'c':
            value_int = 0
            Correct_Flag = False
        elif tmp_box == 'f':
            value_int = -1
            Correct_Flag = False
        else:
            print("Please enter the number or C of check or F of fold.")

    return value_int

#入力された文字がq," ",数字か判断する
def check_data_qc():

    Correct_Flag = True

    while(Correct_Flag):

        tmp_box = input()

        if tmp_box == 'q':
            value = 'q'
            Correct_Flag = False
        elif tmp_box == 'c':
            value = 'c'
            Correct_Flag = False
        else:
            print("Please enter the number or Q of quit or N of next.")

    return value

#場の最大ベット額を更新する
def update_max_bet(max_bet, now_bet, past_bet):
    
    if now_bet + past_bet > max_bet:
        max_bet = now_bet + past_bet
    
    return max_bet

#次の添字にアクセスする
def process_next_index(players_number, now_index, cip_data, cip_index):

    next_index = now_index + 1
    if next_index == players_number:
        next_index = 0
        cip_data, cip_index = add_cip_data(cip_data, cip_index, players_number)

    return next_index, cip_data, cip_index

#次のディーラーボタンにアクセスする
def process_next_dealer(dealer, players_number):

    dealer = dealer + 1
    if dealer == players_number:
        dealer = 0
        
    return dealer

#cip_dataの第二引数に入れるために変換する
def cast_cip(index):
    index += 1
    return index


#cip_dataに新しい配列を追加する
def add_cip_data(cip_data, cip_index, players_number):
    cip_index += 1
    new_array = np.zeros([1,cast_cip(players_number)], dtype=np.int32)
    cip_data = np.concatenate([cip_data, new_array])

    return cip_data, cip_index

#now_playerの現在のラウンドまでの掛け金を求める
def sum_round_bet(round_name, cip_data, cip_index, now_player):

    begin_index = cip_index   
    while(1):
        if cip_data[begin_index][0] == round_name:
            break
        begin_index -= 1

    sum = 0

    for i in range(begin_index, cip_index+1):
        if cip_data[i][cast_cip(now_player)] != -1 and cip_data[i][cast_cip(now_player)] != -2:
            sum +=cip_data[i][cast_cip(now_player)]

    return sum

#前のフェイズにフォールドしているかチェックする
def check_fold(cip_data, cip_index, now_player):
    
    Fold_Flag = False

    if cip_data[cip_index-1][cast_cip(now_player)] == -1:
        Fold_Flag = True
        
    return Fold_Flag

#フォールドした人数を数える
def count_fold(cip_data, cip_index, players_number):
    fold_count = 0
    for i in range(players_number):
            if cip_data[cip_index-1][cast_cip(i)] == -1:
                fold_count += 1
    return fold_count

#プレイしてないことを示す-2を入れる
def full_not_played(cip_data, cip_index, first_player):

    for i in range(first_player+1):
        if cip_data[cip_index][0] != 1:
            if cip_data[cip_index-1][cast_cip(i)] == -1:
                cip_data[cip_index][cast_cip(i)] = -1
        else:
            cip_data[cip_index][cast_cip(i)] = -2

    return cip_data, cip_index