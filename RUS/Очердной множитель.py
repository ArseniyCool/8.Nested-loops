# Программа выводит перемножение можителей в виде столбца
n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(str(i) + ' * ' + str(j) + ' = ' + str(i * j))
