
try:
  print ('Enter a real number to get your fibonacci sequence')
  entry = int(input())
  if entry < 0:
   entry *= -1
  list_1 = []
  def fibonnaci_triangle(number): 
   if number <= 0 or number == 1:
    return number
   elif number > 1:
    result = fibonnaci_triangle(number - 1) + fibonnaci_triangle(number - 2)
    if result not in list_1:
     list_1.append(result)
    if list_1.count(1) < 2:
     list_1.append(1)
    if len(list_1) == entry:
     return list_1
    return result
  print (fibonnaci_triangle(entry))
except:
  print ('it not a correct value'' You must to enter a number value')