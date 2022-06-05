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

#入力された文字をチェックする
def what_do():

    Correct_Flag = True

    while(Correct_Flag):

        tmp_box = input()

        if tmp_box.isnumeric():
            value = int(tmp_box)
            Correct_Flag = False
        elif tmp_box == 'c':
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