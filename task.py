# 1
# cnt = max = 0
# for i in range(1016, 7937 + 1):
#     if i%3==0 and i%7!=0 and i%17!=0 and i%19!=0 and i%27!=0:
#         cnt += 1
#         max = i
# print(cnt, max)

# 2
# hex() - шестнадцетеричная
# x % 16 - последняя цифра в шестнадцетиричная
# x % 256 - возвели в квадрат (дважды совершили операцию)
# print(int('1a', 16))
# print(int('1f', 16))

# чтобы найти две последние цифры в шестн.сс нужно остаток от деления на 16 в квадрате
# cnt = 0
# minx = 100000
# for i in range(2495, 7083 + 1):
#     if (i%256==26 or i%256==31) and i%5!=0 and  i%9!=0:
#         cnt += 1
#         minx = min(minx, i)
# print(cnt, minx)

# 3 новое
# a[i] + a[i+1] - два идущих подряд элемента
# кол-во чисел в файле? 5000 элементов просчитать
# cnt = 0
# maxsim = 0
# a = []
# f = open('17.txt')
# for i in range(5000):
#     a.append(int(f.readline()))
# print(a)

# ищем максимальную сумму, которая делится на 3
# cnt = 0
# maxsum = 0
# a = []
# f = open('17.txt')
# for i in range(5000):
#     a.append(int(f.readline()))
# # снова пробегаемся по этим числам
# # если есть a[i+1] до предпоследнего значения мы должны рассмотреть. Чтобы не было выхода из границы массива
# for i in range(4999):
#     if a[i]%3 == 0 or a[i+1]%3==0:
#         cnt += 1
#         maxsum = max(maxsum, a[i] + a[i+1])
# print(cnt, maxsum)

# 4

# создаем список из строчек
#
# cnt = 0
# mimp = 100000
# a = []
# f = open('17-3.txt')
# s = f.readlines()
# print(s[0]) #5000


# полный код
# cnt = 0
# minp = 1000000
# f = open('17-3.txt')
# a = list(map(int, f.readlines()))
# # print(len(a)) # 5001
# # поскольку у нас существует a[i] + 1, поэтому будет - 1
# for i in range(len(a) - 1):
# # снова пробегаемся по этим числам
# # если есть a[i+1] до предпоследнего значения мы должны рассмотреть. Чтобы не было выхода из границы массива
#     if (a[i] + a[i + 1]) % 7 == 0 and a[i] * a[i + 1] > 0:
#         cnt += 1
#         minp = min(minp, a[i] * a[i+1])
# print(cnt, minp)

# 5
# cnt = 0
# minr = 1000000
# f = open('17-3.txt')
# a = list(map(int, f.readlines()))
# # количество троек просчитать
# for i in range(len(a) - 2):
#     # каждый элемент тройки должен идти в порядке возрастания
#     if a[i] < a[i + 1] < a[i + 2]:
#         # минимальную разность этих элементов
#         r = max(a[i], a[i + 1],a[i + 2]) - min(a[i], a[i + 1], a[i + 2])
#         cnt += 1
#         minr = min(minr, r)
# print(cnt, minr)


# 6
# cnt = 0
# maxs = 0
# f = open('17-204.txt')
# a = list(map(int, f.readlines()))
#
# # a[i + 1] > 0 and a[i+1] %10 == 9 - первое число положительное и оканчивается на 9
# for i in range(len(a) - 2):
#     if a[i + 1] > 0 and a[i+1] %10 == 9 and (a[i] <= 0 or a[i]%10 != 9) and (a[i + 2] <= 0 or a[i+2] %10 != 9):
#         cnt += 1
#         maxs = max(maxs, a[i] + a[i + 1] + a[i + 2])
# print(cnt, maxs)
