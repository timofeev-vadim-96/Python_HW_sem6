# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество 
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def arithm_progr(f_el: int, el_q: int, el_d: int):
    new_list = []
    for n in range(1, el_q+1):
        new_list.append(f_el + (n-1) * el_d)
    return new_list

first_element = int(input('Введите первый элемент арифметической прогрессии: '))
el_quantity = int(input('Введите количество элементов арифметической прогрессии: '))
el_diff = int(input('Введите разность: '))

print(arithm_progr(first_element, el_quantity, el_diff))