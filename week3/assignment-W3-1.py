import json,urllib.request,csv

url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

res = urllib.request.urlopen(url)
original_data = json.loads(res.read().decode("utf-8"))

data = original_data["result"]["results"]

attraction_data = [] #所有景點
mrt_data = [] #所有景點by捷運站
mrt = {} #key:捷運站、value:景點

for i in range(len(data)): #整理attraction_data

  attraction_data.append([
  data[i]["stitle"],
  data[i]["address"][5:8],
  data[i]["longitude"],
  data[i]["latitude"],
  data[i]["file"][0:data[i]["file"].find('https',1)]
  ])

  if (data[i]["MRT"] not in mrt):  #{mrt}整理key:捷運站、value:景點
    mrt[data[i]["MRT"]] = [data[i]["stitle"]]
  else:
    mrt[data[i]["MRT"]].append(data[i]["stitle"])

for (k,v) in mrt.items():  #用{mrt}整理mrt_data格式
  same_mrt = []
  same_mrt.append(k)
  for i in v:
    same_mrt.append(i)
  mrt_data.append(same_mrt)

attraction_csv = open('attraction.csv', 'a+')
write = csv.writer(attraction_csv)
write.writerows(attraction_data)

mrt_csv = open('mrt.csv', 'a+')
write = csv.writer(mrt_csv)
write.writerows(mrt_data)