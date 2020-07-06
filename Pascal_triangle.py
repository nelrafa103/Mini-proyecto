import os
while True:
 try:
  print ('Enter a real number that you want to get the Pascal_triangle')
  entry = int(input())
  os.system('clear')
  def pascal_triangle(number,i,list_2):
   list_1,r = [],0
   if number <= 0:
    return 
   else:
    for x in range(i):
     if len(list_1) == 0 or len(list_1) == i:
      list_1.append(1)
     else:
      list_1.append(sum(list_2[r - 1:r + 1]))
     r += 1
    else:
     list_1.append(1)
   print (list_1)
   return pascal_triangle(number - 1,i + 1,list_1)
  print (pascal_triangle(entry + 1,0,[]))
 except:
  print ('You must to enter a real number')