# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
#  Ввод:                      Ввод:
# 5                           5
# 1 2 3 4 5                   1 5 1 5 1
# Вывод:                      Вывод:
# 0                           2
# (Каждое число вводится с новой строки) 

def list_init(el_count: int) -> list:
    result_list = []
    for i in range(el_count):
        num = int(input('num: '))
        result_list.append(num)
    return result_list

n = int(input('n --> '))
our_list = list_init(n)
print(our_list)

count = 0
for i in range(1, (len(our_list) - 1)):
    if our_list[i - 1] < our_list[i] > our_list[i + 1]:
        count += 1
print(count)        