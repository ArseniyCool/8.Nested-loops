# Программа создаёт новогоднюю ёлку,состающую из поочерёдных чисел
height = int(input('Введите конечное число ёлки:'))
counter = 1
length = 1
while counter <= height:
    for i in range(0, length):
        print(counter, end=' ')
        counter += 1
        if counter > height:
            break
    length += 1
    print('')
