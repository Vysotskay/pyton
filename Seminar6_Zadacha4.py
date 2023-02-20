# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:                Вывод:
# 300                  220 284

# Список делителей для 220: 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110 - их сумма равна 284
# список делителей для 284: 1, 2, 4, 71 и 142 - их сумма равна 220.

def delit(num: int) -> int:
    result_sum = 0
    for i in range(1,(num//2)+1):
        if num%1 == 0:
            result_sum +=i
    return result_sum
k = int(input('k: '))
result = []
for i in range(2, k+1):
    delit_num_1 = delit(i)
    delit_num_2 = delit(delit_num_1)
    duet = {i, delit_num_1}
    if (i == delit_num_2) and (i !=delit_num_1) and (duet not in result):
        result.append(duet)
print(*result)        