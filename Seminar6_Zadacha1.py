# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: 
# 7 
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1                             (каждое число вводится с новой строки)

# Вывод:
# 3 3 2 12


def list_init(el_count: int) -> list:
    result_list = []
    for i in range(el_count):
        num = int(input('num: '))
        result_list.append(num)
    return result_list

n = int(input('n --> '))
m = int(input('m --> '))

first_list = list_init(n)
second_list = list_init(m)
result = []
for item in first_list:
    if item not in second_list:
        result.append(item)
print(result)        
