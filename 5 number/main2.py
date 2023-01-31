# Автомат получает на вход трёхзначное число. По этому числу строится новое число по следующим правилам.

# 1.  Складываются первая и вторая, а также вторая и третья цифры исходного числа.

# 2.  Полученные два числа записываются друг за другом в порядке убывания (без разделителей).

# Пример. Исходное число: 348. Суммы: 3 + 4 = 7; 4 + 8 = 12. Результат: 127. Укажите наименьшее число, в результате обработки которого автомат выдаст число 1412.


for i in range(100, 1000):
    a = i // 100 + i // 10 % 10
    b = i // 10 % 10 + i % 10
    if a > b:
        R = str(a) + str(b)
    else:
        R = str(b) + str(a)
    if R == '1412':
        print(i)
        break