print ('This program got the objetive of make the fibonnnaci sequence')
try:
 entry = int(input())
 def fibonnaci_triangle(number): 
  if number <= 0 or number == 1:
   return number
  elif number > 1:
   return fibonnaci_triangle(number - 1) + fibonnaci_triangle(number - 2) 
 print (fibonnaci_triangle(entry))
except:
  print ('it not a correct value'' You must to enter a number value')