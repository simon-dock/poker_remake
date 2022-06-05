#入力されたデータがint型かチェックする
def int_data():
    
    Correct_Flag = True

    while(Correct_Flag):

        tmp_box = input()

        if tmp_box.isnumeric():
            value_int = int(tmp_box)
            Correct_Flag = False
        else:
            print("Please enter the number.")

    return value_int

#入力された文字がq,"c"判断する
def cq_data():

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
            print("Please enter Q of quit or C of contine.")

    return value

#入力されたデータがint型で2~6かチェックする
def between2and6():
    
    Correct_Flag = True

    while(Correct_Flag):

        tmp_box = input()

        if tmp_box.isnumeric():
            tmp_box = int(tmp_box)
            if tmp_box > 1 and tmp_box < 7:
                value_int = tmp_box
                Correct_Flag = False
        else:
            print("Please enter the number 2~6.")

    return value_int


#入力されたデータがfold_indexないかチェックする
def winner(fold_index):
    
    Correct_Flag = True

    while(Correct_Flag):

        tmp_box = input()

        if tmp_box.isnumeric():
            tmp_box = int(tmp_box)
            if tmp_box <= len(fold_index):
                if fold_index[tmp_box] == 0:
                    value_int = tmp_box
                    Correct_Flag = False
            
        if Correct_Flag == True:
            print("Please enter the number.")

    return value_int


#入力された文字をチェックする
def what_do(players, setting):

    Correct_Flag = True
    now_bet = players[setting.turn].betting

    while(Correct_Flag):

        tmp_box = input()

        if tmp_box.isnumeric():
            value = int(tmp_box)
            if now_bet + value == setting.max_bet:
                Correct_Flag = False
            if now_bet + value >= setting.max_bet*1.25:
                Correct_Flag = False
        elif tmp_box == 'c':
            if now_bet == setting.max_bet:
                value = tmp_box
                Correct_Flag = False
        elif tmp_box == 'f':
            value = tmp_box
            Correct_Flag = False
        elif tmp_box == 'allin':
            value = tmp_box
            Correct_Flag = False
        else:
            print("Please enter the number")
            print("or C of check or F of fold or allin.")

    return value