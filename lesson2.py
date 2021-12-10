#while print('Найти произведение цифр числа.=', mul)
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print('Задача 2')
print('Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.')
sum5 = 0






for i in range(11):
    value = (input('введите числоN:' + str(i)) + '.')
    value = value.strip()
    value = int(float(value))

    print('ЧислоN', i, 'введено', value)
    if value == 5:
        #    print('Это 5!!!!!')
        sum5 += 1
print("введено::::::::::::::::::::::::::::::::::", sum5, "цифр5")
print('Задача 3')
print('Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.')
sum = 0
for i in range(1, 101):
    sum += i
    print(i)
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', i)
    print("Сумма=", sum)

print('Задача 4')
print('Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.')
fact = 1
for i in range(2,11):
    fact*=i


print("произведение=", fact)
print('Задача 4')
print('Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.')
fact = 1
for i in range(2,11):
    fact*=i


print("произведение=", fact)
print('Задача 5')
print('Вывести цифры числа на каждой строчке.')

integer_number = 2129

print(integer_number % 10, integer_number // 10)

while integer_number > 0:
    print(integer_number % 10)
    integer_number = integer_number // 10
print('Найти произведение цифр числа.')
integer_number = 2139413
maxint = 0
current = 0
mul=1
while integer_number > 0:
    current = integer_number % 10
    mul*=current
    if (maxint <= current):
        maxint = current

    print(current, maxint, integer_number // 10)

    integer_number = integer_number // 10
print(current, maxint, integer_number // 10)
print('Произведение=',mul)
print('Задача 8')
print('Дать ответ на вопрос: есть ли среди цифр числа 5?')

integer_number = 2134135
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
        integer_number = integer_number//10
else: print('No')


print('Задача 9')
print('Найти максимальную цифру в числе')
integer_number = 2139413
maxint = 0
current = 0
while integer_number > 0:
    current = integer_number % 10
    if (maxint <= current):
        maxint = current
    print(current, maxint, integer_number // 10)

    integer_number = integer_number // 10
print(current, maxint, integer_number // 10)
print('Max=',maxint)
print('Задача 10')
print('Найти количество цифр 5 в числе')
integer_number = 2139413555
integer_number = 213941355
count5 = 0
current = 0
while integer_number > 0:
    current = integer_number % 10
    if (current==5):
        maxint = current
        count5+=1
    print(current, maxint, integer_number // 10)

    integer_number = integer_number // 10
print(current, maxint, integer_number // 10)
print('5=',count5)


