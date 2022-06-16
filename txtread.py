f = open('myfile.txt', 'r')

datalist = []
while True:
  data = f.readline()
  if data == '':
    break
  print (data.rstrip('\n'))
  datalist.append(data)

print(datalist)
print(type(datalist))
print(type(datalist[1]))

f.close()

f = open('myfile.txt', 'w')

datalist = []
game_count = 4
datalist.append("# poker_remake\n")
datalist.append("## Count of game\n")
datalist.append(str(game_count) +"\n")
datalist.append("\n")
f.writelines(datalist)

datalist = []
for i in range(4):
  datalist.append("Name\n")
  datalist.append(str(i)+"\n")
  datalist.append("cip\n")
  datalist.append(str(i) +"\n")
  datalist.append("win\n")
  datalist.append(str(i) +"\n")
  datalist.append("join\n")
  datalist.append(str(i) +"\n")
  datalist.append("raise\n")
  datalist.append(str(i) +"\n")
  datalist.append("allin\n")
  datalist.append(str(i) +"\n")
  datalist.append("cip_log\n")
  datalist.append(str(i) +"\n")
  tmp = "\n"
  datalist.append(tmp)
  
    
f.writelines(datalist)

f.close()