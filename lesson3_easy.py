# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number = number * (10**ndigits) + 0.4
    return int(number) / (10**ndigits)



print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    first = list(str(ticket_number))[:3]
    second = list(str(ticket_number))[3:]
    sum1 = 0
    sum2 = 0
    for i in range(3):
        sum1 += int(first[i])
        sum2 += int(second[i])
    if sum1 == sum2:
        return "Билет является счастливым"
    else:
        return "Билет не является счастливым"


print(lucky_ticket(123006))
print(lucky_ticket(123210))
print(lucky_ticket(436751))