# Mama
print("Множества")

print("Задание 1")
data1 = {1,2,2,3,4,4,5}
print(data1)
print(len(set(data1)))

print("Задание 2")
data2 = {1,2,3}
data2.add(4)
data2.remove(3)
print(data2)

print("Задание 3")
data3 = {1,2,3,4}
dat3 = {4,5,6,7}
print(data3 | dat3)

print("Задание 4")
data4 = {1,2,3,4}
dat4 = {4,5,6,7}
print(data4 & dat4)

print("Задание 5")
data5 = {2,3,4,5}
dat5 = {3,4,5,6}
print(data5 - dat5)
print(dat5 - data5)

print("Задание 6")
data6 = {2,3,4}
dat6 = {1,2,3,4,5,6}
print(data6 ^ dat6)

print("Задание 7")
data7 = {1,2,3,4}
x = 3
if x in data7:
    print("Число", x, "есть в множестве")
else:
    print("Число", x, "отсутствует в множестве")

print("Задание 8")
data8 = {5,6}
dat8 = {5,6,7,8}
print(data8.issubset(dat8))
print(dat8.issubset(data8))

print("Задане 9")
str1 = "водогрязеторфопарафинолечение"
simvoly = set(str1)
print(simvoly)
print(len(simvoly))

print("Задание 10")
spisok1 = [1,2,2,3,4,4]
spis1 = [3,1,5,5,6,4]
set1 = set(spisok1)
set2 = set(spis1)
peresechenie = set1 & set2
itog = sorted(peresechenie)
print(itog)

print("Кортежи")

print("Задание 1")
g1 = (83, 52, 67, 54, 76)
print(g1[0])
print(g1[2])
print(g1[-1])

print("Задание 2")
g2 = (1,2,3,4,5,6,7,8)
print(g2[0])
print(g2[1])
print(g2[-2])
print(g2[-1])
print(g2[::-1])

print("Задание 3")
g3 = (12,34,56,78,90)
print(len(g3))
print(sum(g3))
print(min(g3))
print(max(g3))

print("Задание 4")
g4 = (23,45,67,89)
x = 67
if x in g4:
    print("Число", x, "есть в кортеже")
    print(g4.index(x))
    print(g4.count(x))
else:
    print("Число", x, "отсутствует в кортеже")

print("Задание 5")
g5 = (1,2,3,4,5)
gg5 = (6,7,8,9,10)
ggg5 = g5 + gg5
print(ggg5)

print("Задание 6")
g6 = (4,)
print(type(g6))

print("Задание 7")
name, age, city = ("Иван", 25, "Москва")
print(name)
print(age)
print(city)

print("Задание 8")
g8 = 5
gg8 = 10
print("до", g8, gg8)
g8, gg8 = gg8, g8
print("после", g8, gg8)

print("Задание 9")
g9 = (10, 20, 30, 40)
gg9 = g9[:1] + (99,) + g9[2:]
print(gg9)

print("Задание 10")
g10 = (5, 3, 5, 1, 3, 8, 1)
gg10 = tuple(sorted(set(g10)))
print(gg10)
