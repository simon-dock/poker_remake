def result(players):

    f = open('README.md', 'r')

    readlist = []
    count = 0
    while True:
        raw_data = f.readline()
        if raw_data == '':
            break
        data = raw_data.rstrip('\n')
        if data.isnumeric():
            tmp_box = int(data)
            readlist.append(tmp_box)
        if count % 20 == 5:
            tmp_box = data.split()
            readlist.append(tmp_box[1])
        count += 1

    f.close()

    f = open('README.md', 'w')

    datalist = []
    game_count = len(players[0].log_cip)-1
    datalist.append("# poker_remake\n")
    datalist.append("## Count of game\n")
    datalist.append(str(game_count+readlist[0]) +"\n")
    datalist.append("times\n")
    datalist.append("\n")
    joined_player = []
    for i in range(len(players)):
        for j in range(len(readlist)):
            if readlist[j] == players[i].name:
                joined_player.append(j)
                break
        datalist.append("### "+players[i].name +"\n")
        datalist.append("* The number of times you joined in the game.  \n")
        game_joined = game_count+readlist[j+1]
        datalist.append(str(game_joined) +"\n")
        datalist.append("times\n")

        datalist.append("* Total of cip you have.  \n")
        datalist.append(str((players[i].cip-players[i].initial_cip)+readlist[j+2]) +"\n")
        datalist.append("$\n")

        datalist.append("* The number of times you won & percentage.  \n")
        win_count =players[i].log_win+readlist[j+3]
        datalist.append(str(win_count) +"\n")
        datalist.append("times, "+str((win_count/game_joined)*100)+"%\n")

        datalist.append("* The number of times you joined in Preflop & percentage.  \n")
        prejoin_count =players[i].log_join+readlist[j+4]
        datalist.append(str(prejoin_count) +"\n")
        datalist.append("times, "+str((prejoin_count/game_joined)*100)+"%\n")

        datalist.append("* The number of times you Raise.  \n")
        datalist.append(str(players[i].log_raise+readlist[j+5]) +"\n")
        datalist.append("times\n")

        datalist.append("* The number of times you Allin.  \n")
        datalist.append(str(players[i].log_allin+readlist[j+6]) +"\n")
        datalist.append("times\n")

        datalist.append("\n")

    for i in range(6):
        Do_Flag = True
        name_number = i*7+1
        
        for j in range(len(joined_player)):
            if joined_player[j] == name_number:
                Do_Flag = False

        if Do_Flag == True:
            datalist.append("### "+str(readlist[name_number]) +"\n")
            datalist.append("* The number of times you joined in the game.  \n")

            datalist.append(str(readlist[name_number+1]) +"\n")
            datalist.append("times\n")

            datalist.append("* Total of cip you have.  \n")
            datalist.append(str(readlist[name_number+2]) +"\n")
            datalist.append("$\n")

            datalist.append("* The number of times you won & percentage.  \n")
            win_count =readlist[name_number+3]
            datalist.append(str(win_count) +"\n")
            if readlist[name_number+1] == 0:
                rate = 0
            else:
                rate = win_count/readlist[name_number+1]*100
            datalist.append("times, "+str(rate)+"%\n")

            datalist.append("* The number of times you joined in Preflop & percentage.  \n")
            prejoin_count =readlist[name_number+4]
            datalist.append(str(prejoin_count) +"\n")
            if readlist[name_number+1] == 0:
                rate = 0
            else:
                rate = prejoin_count/readlist[name_number+1]*100
            datalist.append("times, "+str(rate)+"%\n")

            datalist.append("* The number of times you Raise.  \n")
            datalist.append(str(readlist[name_number+5]) +"\n")
            datalist.append("times\n")

            datalist.append("* The number of times you Allin.  \n")
            datalist.append(str(readlist[name_number+6]) +"\n")
            datalist.append("times\n")

            datalist.append("\n")
        
        
    f.writelines(datalist)

    f.close()