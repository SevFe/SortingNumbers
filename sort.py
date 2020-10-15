# Take input from user and put into list
# Setting up lists
# Finding length of listNum (list of user input)
# Reversed version of listNum is re_list
# Assign a count to each item in listNum and append that to 
# count_list
# Compares the counts and items in listNum. comparison_list is in   
# descending order

# Take input from user and put into list

listPre = input("Input space-separated numbers: ").split()

listNum = list(map(int, listPre))

# Setting up lists

re_list = []
comparison_list = []
count_list = []

# Finding length of listNum

leng = len(listNum)

# Reversed version of listNum is re_list

for n in range(leng - 1, -1, -1):
  re_list.append(listNum[n])

# Assign a count to each item in listNum and append that to 
# count_list

for x in range(len(listNum)):
  count = 0
  for y in range(len(re_list)):
    if listNum[x] < re_list[y]:
      count += 1
  count_list.append(count)

# Compares the counts and items in listNum. comparison_list is in   
# descending order

for i in range(len(count_list)):
  comparison_list.append(listNum[count_list.index(i)])

print(comparison_list)
