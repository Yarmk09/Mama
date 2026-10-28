# Mama
print("Словари")

print("Задание 1")
marks = {"Anton":4, "Iaroslav":5, "Igor":3}
print(marks["Iaroslav"])

print("Задание 2")
marks = {"Anton": 4, "Iaroslav": 5, "Igor": 3}
marks["Masha"] = 5
marks["Anton"] = 3
del marks["Igor"]
print(marks)

print("Задание 3")
marks = {"Anton": 4, "Iaroslav": 5, "Igor": 3}
key = "Petr"
print(marks.get(key, "Нет такого ключа"))

print("Задание 4")
marks = {"Anton": 4, "Iaroslav": 5, "Igor": 3}
print(marks.keys())
print(marks.values())
print(len(marks))

print("Задание 5")
prroducts = {"Вилла":589000000.99, "Квартира":8000000.99, "Дом":25000000.99}
for name, price in prroducts.items():
    print(name, price)

print("Задание 6")
prroducts = {"Вилла":589000000.99, "Квартира":8000000.99, "Дом":25000000.99}
total = sum(prroducts.values())
print("Сумма всех цен:", total)
dorogoy = max(prroducts, key=prroducts.get)
print("Самый дорогой товар:", dorogoy, prroducts[dorogoy])

print("Задание 7")
str1 = "abracadabra"
counts = {}
for ch in str1:
    if ch in counts:
        counts[ch] += 1
    else:
        counts[ch] = 1
print(counts)

print("Задание 8")
str2 = "вчера я видел сон , очень странный сон"
words = str2.split()
counts = {}
for gg in words:
    counts[gg] = counts.get(gg, 0) + 1
print(counts)
print("Самое частое:", max(counts, key=counts.get))

print("Задание 9")
marks = {"Anton": 4, "Iaroslav": 5, "Igor": 3}
perevernyl = {}
for name, mark in marks.items():
    perevernyl[mark] = name
print(perevernyl)

print("Задание 10")
print("Страны: Россия, Франция, Германия")
strani = ["Россия", "Франция", "Германия"]
stolitsi  = ["Москва", "Париж", "Берлин"]
d = {}
for i in range(len(strani)):
    d[strani[i]] = stolitsi[i]
country = input("Введите страну: ")
print(d[country])

print("Циклы")

print("for")

print("Задание 1")
for i in range(1,11):
    print(i)

print("Задание 2")
for i in range(2,51,2):
    print(i)

print("Задание 3")
for i in range(1,11):
    continue
print(i)

print("Задание 4")
n = int(input("Введите n: "))
s = 0
for i in range(1, n + 1):
    s += i
print("Сумма =", s)

print("Задание 5")
n = int(input("Введите n: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"{n}! = {fact}")

print("Задание 6")
n = int(input("Введите число n: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

print("Задание 7")
chisla = [3, -1, 0, 5, -7, 8, 2, -4, 0, 6]
count = 0
for x in chisla:
    if x > 0:
        count += 1
print("Положительных чисел:", count)

print("Задание 8")
text = input("Введите строку: ")
glasniy = "аеёиоуыэюя"
count = 0
for ch in text.lower():
    if ch in glasniy:
        count += 1
print("Гласных букв:", count)

print("Задание 9")
numbers = [3, -1, 0, 5, -7, 8, 2, -4, 0, 6]
maximum = numbers[0]
for x in numbers:
    if x > maximum:
        maximum = x
print("Наибольший элемент:", maximum)

print("Задание 10")
print("Не знаю как делать")

print("while")

print("Задание 1")
i = 1
while i <= 10:
    print(i)
    i += 1

print("Задание 2")
itog = 0
number = int(input("Введите число (0 — для завершения): "))
while number != 0:
    itog += number
    number = int(input("Введите число (0 — для завершения): "))
print("Сумма введённых чисел:", itog)

print("Задание 3")
number = int(input("Введите натуральное число: "))
count = 0
while number > 0:
    number //= 10
    count += 1
print("Количество цифр:", count)

print("Задание 4")
number = int(input("Введите натуральное число: "))
total = 0
while number > 0:
    total += number % 10
    number //= 10
print("Сумма цифр:", total)

print("Задание 5")
number = int(input("Введите натуральное число: "))
result = ""
while number > 0:
    result += str(number % 10)
    number //= 10
print("Число в обратном порядке:", result)

print("Задание 6")
n = int(input("Введите число n: "))
stepen = 1
while stepen <= n:
    print(stepen)
    stepen = stepen * 2

print("Задание 7")
passw = "12345"
input_passw = input("Введите пароль: ")
while input_passw != passw:
    print("Неверный пароль")
    input_passw = input("Введите пароль: ")
print("Доступ разрешен")

print("Задание 8")
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
num1, num2 = a, b
while b > 0:
    a, b = b, a % b
print(f"Наибольший общий делитель чисел {num1} и {num2} равен: {a}")

print("Задание 9")
n = int(input("Введите число n: "))
current = 0
next_num = 1
while current <= n:
    print(current, end=" ")
    future = current + next_num
    current = next_num
    next_num = future

print("Задание 10")
print("Не знаю как делать")
