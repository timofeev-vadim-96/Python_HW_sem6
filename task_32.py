# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random
new_list = [random.randint(1,100) for x in range (10)]
print(new_list)

def determ_ind(input_list, l_b, r_b):
    indices_list = []
    for i in input_list:
        if l_b <= i <= r_b:
            indices_list.append(input_list.index(i))
    return indices_list

left_b = int(input('Введите левую границу: '))
right_b = int(input('Введите правую границу: '))
print(determ_ind(new_list, left_b, right_b))