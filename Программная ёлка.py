# Программа создаёт новогоднюю ёлку,
# состающую из заданного символа и украшенную новогодними шариками
height = int(input('Введите число шариков:'))
symbol = input('Введите вид шара(Символ):')
counter = 1
length = 1
while counter <= height:
    for i in range(0, length):
        print(symbol, end=' ')
        counter += 1
        if counter > height:
            break
    length += 1
    print('')
