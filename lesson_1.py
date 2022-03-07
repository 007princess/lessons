# 1
a = str(input())
print(a)
# 2
b = str(input('Введи предложение из 3 слов: '))
b1 = b.replace(' ','!')
print(b1)
#3
m = 'Информатика'
m1 = m[0:2]
m2 = m[6:10]
m3 = m[1:5]
print(m1, m2, m3)
#4
c = int(input('Введи первое число: '))
d = int(input('Введи второе число: '))
e = int(input('Введи третье число: '))
f = int((c+d+e)**2)
g = int((c-d-e)**2)
print('Кврадрат суммы =',f)
print('Кврадрат разности =',g)

