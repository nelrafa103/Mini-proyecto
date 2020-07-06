import os

def clear_console():
  if os.name == "posix":
    os.system('clear')
  elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    os.system('cls')

while(True):
		try:
			entry = int(input('How many fibonacci numbers do you want? '))
			if type(entry) != int:
				raise ValueError
			if entry < 1:
				raise TypeError 
			break
		except (ValueError):
			print('\nEnter a numeric value\n')
		except (TypeError):
				print('\nEnter a positive value\n')

list_1 = []

def fibonnaci_triangle(number): 
  clear_console()
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

next = input('\nThese are the first {} issues of the fibonacci series...'.format(entry))
