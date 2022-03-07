# задание 1
a = int(input())
b = int(input())
if a == b:
    print('a равно b')
else:
    print('a не равно b')

# Задание 2
a = int(input())
if a % 2 == 0:
    print('кратно')
else:
    print('некратно')

# Задание 3
d = []
for i in range(3):
    d.append(int(input()))
print(max(d))

# Задание 4
a = [9, 6, 10, 13, 1]
a.sort()
print(len(a))

# Задание 5
a = [8, 3, 1, 1, 9, 1]
b = a.count(1)
if b % 3 == 0:
    print('кратно')
else:
    print('некратно')
print(b)

# Задание 6
def function(x, z):
    y = x ** 2 - z * x + 5 * z
    return y
print(function(3, 2))

# Задание 7
a = [7, 11, 13, 18, 40]
print(a)
a.pop(0)
print(a)