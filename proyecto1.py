
def triangulo_de_fibonnaci(number): 
 result =  number
 if number <= 0:
  return result
 elif number > 1:
  result = triangulo_de_fibonnaci(number - 1) + triangulo_de_fibonnaci(number - 2)  
 return result
print (triangulo_de_fibonnaci(1))