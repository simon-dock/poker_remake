
def result(players):
    f = open('myfile.txt', 'w')

    datalist = []
    game_count = len(players[0].log_cip)-1
    datalist.append("Count of game\n")
    datalist.append(str(game_count) +"\n")
    datalist.append("\n")
    f.writelines(datalist)
    
    datalist = []
    for i in range(len(players)):
        datalist.append("name\n")
        datalist.append(players[i].name +"\n")
        datalist.append("cip\n")
        datalist.append(str(players[i].cip) +"\n")
        datalist.append("win\n")
        datalist.append(str(players[i].log_win) +"\n")
        datalist.append("join\n")
        datalist.append(str(players[i].log_join) +"\n")
        datalist.append("raise\n")
        datalist.append(str(players[i].log_raise) +"\n")
        datalist.append("allin\n")
        datalist.append(str(players[i].log_allin) +"\n")
        datalist.append("cip_log\n")
        datalist.append(str(players[i].log_cip) +"\n")
        tmp = "\n"
        datalist.append(tmp)
        
        
    f.writelines(datalist)

    f.close()