# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.

def replace_marks(marks_list):
    for i in range(len(marks_list)):
        if (marks_list[i] == 5) or (marks_list[i] == 4):
            marks_list[i] = 2
    return marks_list


marks = [4, 2, 2, 1, 5, 5]
print(replace_marks(marks))

