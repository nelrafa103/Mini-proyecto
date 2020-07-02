
def fibonnaci_triangle(number): 
 print (number,end = ' ')
 if number <= 0 or number == 1:
  return number
 elif number > 1:
  return fibonnaci_triangle(number - 1) + fibonnaci_triangle(number - 2)
print (fibonnaci_triangle(6))