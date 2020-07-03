print ('This program got the objetive of make the fibonnnaci sequence')
try:
 entry = int(input())
 list_1 = []
 def fibonnaci_triangle(number): 
  if number <= 0 or number == 1:
   return number
  elif number > 1:
   result = fibonnaci_triangle(number - 1) + fibonnaci_triangle(number - 2)
   if result not in list_1:
    list_1.append(result)
   return result
 print (fibonnaci_triangle(entry))
except:
  print ('it not a correct value'' You must to enter a number value')