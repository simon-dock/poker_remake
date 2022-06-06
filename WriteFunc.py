
def result(players):
    f = open('myfile.txt', 'w')

    datalist = []
    for i in range(len(players)):
        tmp = players[i].name +"\n"
        datalist.append(tmp)
        tmp = str(players[i].cip) +"\n"
        datalist.append(tmp)
        tmp = str(players[i].log_win) +"\n"
        datalist.append(tmp)
        tmp = str(players[i].log_join) +"\n"
        datalist.append(tmp)
        tmp = str(players[i].log_raise) +"\n"
        datalist.append(tmp)
        tmp = str(players[i].log_allin) +"\n"
        datalist.append(tmp)
        tmp = str(players[i].log_cip) +"\n"
        datalist.append(tmp)
        tmp = "\n"
        datalist.append(tmp)
        
        
    f.writelines(datalist)

    f.close()