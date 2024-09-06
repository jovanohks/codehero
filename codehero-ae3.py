list = [82, 2, 28, 2, 2, 28, 35, 87, 38, 97, 71, 38, 99, 98, 31, 2, 48, 2, 48, 84, 2, 6, 24, 38, 46, 21, 32, 52, 68, 65, 51, 2, 58, 2, 83]
largestlistcount=0
for i in range(1,len(list)):
  listcount= list.count(list[i])
  if listcount > largestlistcount:
    largestlistcount=listcount
    numiter=list[i]
print(numiter)
