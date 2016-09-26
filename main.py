import math

print("Введите а: ")
a = float(input())
print("Введите b: ")
b = float(input())
print("Введите n: ")
n = int(input())

interval = (b - a) / n
c = (b - a) / 2

square_integral_left = 0
square_integral_right = 0
square_integral_mid = 0
teylor = math.sin(c)



for i in range(n):
    square_integral_left += math.sin(i * interval) * ((i + 1) * interval - i * interval)
    square_integral_right += math.sin((i + 1) * interval) * ((i + 1) * interval - i * interval)
    square_integral_mid += math.sin(((i + 1) * interval + i * interval) / 2) * ((i + 1) * interval - i * interval)
    teylor += math.sin(c + math.pi*i/n) * (b - c) ** (n + 1) / (math.factorial(n) * (n + 1)) - \
              math.sin(c + math.pi*i/n) * (a - c) ** (n + 1) / (math.factorial(n) * (n + 1))


print("Прямоугольники: ")
print("Левый: {0:.5f}, правый {1:.5f}, середина: {2:.5f}".format(square_integral_left,
                                                                 square_integral_right,
                                                                 square_integral_mid))
print("Трапеции: {0:.5f}".format((square_integral_left + square_integral_right) / 2))
print("Тейлор: {0:.5f}".format(teylor))

print("Проверка: {0:.5f}".format(math.cos(a) - math.cos(b)))


