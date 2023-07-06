while True:
    n = input('Введите целое положительное число n:')
    if n.isdigit():
        print('Получилась последовательность:')
        break
for i in range(int(n)+1):
    for j in range(i):
        print(i, end='')