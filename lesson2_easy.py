# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"] 
for fruit in fruits:
    print('{:>10}'.format(fruit))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
    
a = [1, 3, 'fb', 65, 4]
b = [3, 'fb', 10.5]
a_new = set(a)
b_new = set(b)
a_new.difference_update(a_new.intersection(b_new))
a = list(a_new)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

a = [1, 65, 7, 4, 3]
for each in a:
    if each % 2 == 0:
        each = each / 4
    else:
        each = each * 2
