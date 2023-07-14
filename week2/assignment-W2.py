print ("=== Task 1 ===")

def find_and_print(messages):  #時間複雜度 O(k*j*n)

# write down your judgment rules in comments
# 設定>17的規則關鍵字，並檢查若含否定句關鍵字(not、n't)則需剃除

# your code here, based on your own rules
  #>17的規則關鍵字
  judge_rules = ['18 years old', 'college student', 'legal age in Taiwan', 'vote for Donald Trump']
  #user言論否定句關鍵字
  negative_sentences = ['not','n\'t']

  for (k,v) in messages.items():
    #user言論若包含規則關鍵字
    for rule in judge_rules:
      if rule in v:
        flag = 0
        #檢查user言論無包含否定句關鍵字
        for negative in negative_sentences:
          if negative not in v:
            flag += 1

            if flag == len(negative_sentences):
              print(k)

find_and_print({
"Bob":"My name is Bob. I'm 18 years old.",
"Mary":"Hello, glad to meet you.",
"Copper":"I'm a college student. Nice to meet you.",
"Leslie":"I am of legal age in Taiwan.",
"Vivian":"I will vote for Donald Trump next week",
"Jenny":"Good morning."
})

print ("=== Task 2 ===")

def calculate_sum_of_bonus(data):  #時間複雜度 3*O(n)

# write down your bonus rules in comments
#以獎金發放較薪資之月數為激勵方式，下列為3個role各自performance加權，主要考量原因說明：
#1. Sales績效對營收波動影響較短期顯著，故在above average 加權最多為3倍、below average波動亦較Engineer大為0.3倍
#2. CEO之Salary最多，故above average加權最少為1.5倍;此外錯誤的決策對公司影響鉅大，故其below average倍數最低為0.1倍

#Engineer={"above average":2,"average":1,"below average":0.5}
#CEO={"above average":1.5,"average":1,"below average":0.1} 
#Sales={"above average":3,"average":1,"below average":0.3}

# your code here, based on your own rules

  #資料文字處理
  for i in range(3):
    if ("USD" in str(data["employees"][i]["salary"])):
      data["employees"][i]["salary"] = int(data["employees"][i]["salary"].replace("USD", ""))*30
    data["employees"][i]["salary"] = int(str(data["employees"][i]["salary"]).replace(",", ""))

  #獎金加權倍數by role及performance
  bonus_ratio = {"Engineer":{"above average":2,"average":1,"below average":0.5},
  "CEO":{"above average":1.5,"average":1,"below average":0.1},
  "Sales":{"above average":3,"average":1,"below average":0.3}}

  #考量salary後之獎金加權小計
  bonus_raw = 0
  for i in range(3):
    salary = data["employees"][i]["salary"]
    role = data["employees"][i]["role"]
    performance = data["employees"][i]["performance"]
    bonus_raw += salary*bonus_ratio[role][performance]

  #在獎金10000下，基本獎金(average)倍數比例 = 10000/獎金加權小計
  bonus_month_ratio = 10000/bonus_raw

  #每人分配到獎金較薪資之月數
  bonus_month = {} 
  #每人分配到獎金amount
  bonus_list = {}
  bonus = 0

  for i in range(3):
    salary = data["employees"][i]["salary"]
    role = data["employees"][i]["role"]
    performance = data["employees"][i]["performance"]
    name = data["employees"][i]["name"]

    bonus_month[name] = bonus_month_ratio*bonus_ratio[role][performance]
    bonus_list[name] = round(salary*bonus_month[name])

    bonus += bonus_list[name]
  #每人分配到獎金較薪資之月數
  #print(bonus_month) {'John': 0.148148, 'Bob': 0.074074, 'Jenny': 0.02222}
  #每人分配到獎金amount {'John': 4444, 'Bob': 4444, 'Jenny': 1111}
  #print(bonus_list)

  print(bonus)

calculate_sum_of_bonus({
"employees":[
{
"name":"John",
"salary":"1000USD",
"performance":"above average",
"role":"Engineer"
},
{
"name":"Bob",
"salary":60000,
"performance":"average",
"role":"CEO"
},
{
"name":"Jenny",
"salary":"50,000",
"performance":"below average",
"role":"Sales"
}
]
}) # call calculate_sum_of_bonus function

print("=== Task 3 ===")

def func(*data):  #時間複雜度 2*O(m*n)

# your code here
  middle_name = {}
  unique_name = []
  # 統計每個middle name 出現次數
  for name in data:
    for i in range(1, len(name)):
      if name[i] not in middle_name:
        middle_name[name[i]] = 1
      else:
        middle_name[name[i]] += 1    

  for name in data:
      flag_unique_name = 1
      for i in range(1, len(name)):
        flag_unique_name *= middle_name[name[i]]
        # 若middle name出現次數相乘為4(2*2)，則為疊字的情形
        if flag_unique_name == 4: 
          if (i == 2) & (name[i] == name[i-1]):
            unique_name.append(name)
      # 若middle name出現次數相乘為1則表示沒跟其他名字重複      
      if flag_unique_name == 1:
        unique_name.append(name)

  for unique in unique_name:
      print(unique)

  if len(unique_name) == 0:
      print('沒有')

func("彭⼤牆", "王明雅", "吳明") # print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有

print("=== Task 4 ===")

def get_number(index): #時間複雜度 O(1)
# your code here

  print(index//2 *3 + index%2 *4)

get_number(1) # print 4
get_number(5) # print 10
get_number(10) # print 15

print("=== Task 5 ===")

def find_index_of_car(seats, status, number): #時間複雜度 O(n)
# your code here
  ans = -1
  for i in range(len(status)):
    # car status can serve
    if status[i] == 1:
      #car空位足以容納需求
      if seats[i] >= number:
        #若第一次則記錄車號及diff = seats[i] - number
        if (ans == -1):
          diff = seats[i] - number
          ans = i
        #若非第一次則比較是否有diff更小的較適合解
        else:
          if (seats[i] - number <= diff):
            diff = seats[i] - number
            ans = i            
  print (ans)

find_index_of_car([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2) # print 4
find_index_of_car([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find_index_of_car([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2

print("=== Additional Task 1 ===")

def max_product(nums):   #時間複雜度 O(n^2)
# your code here 

  for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
      if i == 0:
        ans = nums[i]*nums[j]
      else:
        if nums[i]*nums[j] > ans:
          ans = nums[i]*nums[j]
  print (ans)

max_product([5, 20, 2, 6]) # print 120 
max_product([10, -20, 0, 3]) # print 30 
max_product([10, -20, 0, -3]) # print 60 
max_product([-1, 2]) # print -2 
max_product([-1, 0, 2]) # print 0 
max_product([5,-1, -2, 0]) # print 2 
max_product([-5, -2]) # print 10 

print("=== Additional Task 2 ===")

def two_sum(nums, target):  #時間複雜度 O(n^2)
  # your code here 
  for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
      if nums[i]+nums[j] == target:
        return [i,j]
result=two_sum([2, 11, 7, 15], 9) 
print(result) # show [0,2] because nums[0]+nums[2] is 9 
