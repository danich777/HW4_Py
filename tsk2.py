# B. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import random


def create_koef(k):
    lst = [random.randint(0, 100) for i in range(k + 1)]
    return lst


def create_str_poly(sp):
    lst = sp[::-1]
    equantion = ''
    if len(lst) < 1:
        equantion = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                equantion += f'{lst[i]}x^{len(lst) - i - 1}'
                if lst[i + 1] != 0 or lst[i + 2] != 0:
                    equantion += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                equantion += f'{lst[i]}x'
                if lst[i + 1] != 0 or lst[i + 2] != 0:
                    equantion += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                equantion += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                equantion += ' = 0'
    return equantion

def get_pow(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i + 1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num


def get_koef(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num


def decon_poly(equantion):
    equantion = equantion[0].replace(' ', '').split('=')
    equantion = equantion[0].split('+')
    lst = []
    l = len(equantion)
    k = 0
    if get_pow(equantion[-1]) == -1:
        lst.append(int(equantion[-1]))
        l -= 1
        k = 1
    i = 1  # ст
    ii = l - 1  # инд
    while ii >= 0:
        if get_pow(equantion[ii]) != -1 and get_pow(equantion[ii]) == i:
            lst.append(get_koef(equantion[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1

    return lst


def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)

k1 = int(input("Введите натуральную степень первого многочлена k: "))
k2 = int(input("Введите натуральную степень второго многочлена k: "))
koef1 = create_koef(k1)
koef2 = create_koef(k2)
write_file("file1.txt", create_str_poly(koef1))
write_file("file2.txt", create_str_poly(koef2))

with open('file1.txt', 'r') as data:
    st1 = data.readlines()
with open('file2.txt', 'r') as data:
    st2 = data.readlines()
print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")
lst1 = decon_poly(st1)
lst2 = decon_poly(st2)
ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(ll)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll, mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll, mm):
        lst_new.append(lst2[i])
write_file("file_res.txt", create_str_poly(lst_new))
with open('file_res.txt', 'r') as data:
    st3 = data.readlines()
print(f"Результирующий многочлен {st3}")