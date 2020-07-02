
x = int(input())
def fibonnaci_triangle(number): 
 try:
  print (number,end = ' ')
  if number <= 0 or number == 1:
   return number
  elif number > 1:
   return fibonnaci_triangle(number - 1) + fibonnaci_triangle(number - 2)
 except:
  return 'Debe ingresar un numero real'
print (fibonnaci_triangle(x))

