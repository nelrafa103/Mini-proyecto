try:
 entry = int(input())
 def pascal_triangle(number):
  print (number)
  if number <= 0:
   return 
  else:
   return pascal_triangle(number - 1) + pascal_triangle(number - 2)
 print (pascal_triangle(entry))
except:
 print ('Debe ingresar el numero de filas en numeros reales')