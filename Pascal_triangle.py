import os


def clear_console():
    if os.name == "posix":
        os.system('clear')
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system('cls')


while(True):
    try:
        entry = int(input("how many rows of pascal's triangle do you want? "))
        if type(entry) != int:
            raise ValueError
        if entry < 1:
            raise TypeError
        break
    except (ValueError):
        print('\nEnter a numeric value\n')
    except (TypeError):
        print('\nEnter a positive value\n')


def pascal_triangle(number, i, list_2):
    list_1, r = [], 0
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
    print(' ' * number, list_1)
    return pascal_triangle(number - 1, i + 1, list_1)


print(pascal_triangle(entry + 1, 0, []))

next = input("\nThe first {} rows of pascal's triangle...".format(entry))
