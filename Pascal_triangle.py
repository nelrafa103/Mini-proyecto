while True:
 try:
  print ('Enter a real number that you want to get the Pascal_triangle')
  entry = int(input())
  def pascal_triangle(number,i):
   list_1 = [[]] * number
   if number <= 0:
    return list_1
   else:
    for x in range(i):
     if len(list_1) > 1 or :
      list_1.append()
    else:
     list_1[0].append(1)
   return pascal_triangle(number - 1,i + 1)
  print (pascal_triangle(entry,0))
 except:
  print ('You must to enter a real number')