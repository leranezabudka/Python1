# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib = []
    a, b = 0, 1
    for num in range(m):
        fib.append(b)
        a, b = b, a + b
    return fib[n-1:m]

print(fibonacci(3, 7))
        

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for i in range(len(origin_list)):
        for j in range(len(origin_list)):
            if origin_list[i] <= origin_list[j]:
                origin_list[i], origin_list[j] = origin_list[j], origin_list[i]
    return origin_list                


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(func, b):
    for i in b:
        if func(i) == False:
            b.remove(i)
    return(b)

def func(a):
    if a > 0:
        return True
    return False


print(my_filter(func, [1,-1,2,0]))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
from math import sqrt

def paral(x1, y1, x2, y2, x3, y3, x4, y4):
    l1 = sqrt((x1-x2)**2 + (y1-y2)**2)
    l2 = sqrt((x3-x2)**2 + (y3-y2)**2)
    l3 = sqrt((x3-x4)**2 + (y3-y4)**2)
    l4 = sqrt((x1-x4)**2 + (y1-y4)**2)
    if l1 == l3 and l2 == l4:
        return "Эти точки являются вершинами параллелограмма"
    return "Эти точки не являются вершинами параллелограмма"

print(paral(0,0,1,3,4,3,3,0))
print(paral(0,0,1,3,4,2,3,0))