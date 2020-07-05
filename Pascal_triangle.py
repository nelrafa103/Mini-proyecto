while True:
 try:
  print ('Enter a real number that you want to get the Pascal_triangle')
  entry = int(input())
  def pascal_triangle(number,i):
   list_1 = [] 
   r = 0
   if number <= 0:
    return 
   else:
    for x in range(i):
     if len(list_1) == 1:
      list_1.append(sum(list_1))
     else:
      list_1.append(sum(list_1))
    else:
     list_1.append(1)
   print (list_1,'U.U')
   return pascal_triangle(number - 1,i + 1)
  print (pascal_triangle(entry,0))
 except:
  print ('You must to enter a real number')