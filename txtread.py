f = open('README.md', 'r')

datalist = []
count = 0
while True:
  raw_data = f.readline()
  if raw_data == '':
    break
  data = raw_data.rstrip('\n')
  if data.isnumeric():
    tmp_box = int(data)
    datalist.append(tmp_box)
  if count % 20 == 5:
    tmp_box = data.split()
    datalist.append(tmp_box[1])
  count += 1

print(datalist)

f.close()
