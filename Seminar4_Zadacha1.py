# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# sp = input().split()
# result = {}
# for i in sp:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#     else:
#         print(i, end=' ')
#         result[i] = result.get(i, 0) + 1

# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Hello word!

our_string = "Hello word!"
our_dict ={}
count_list = set(our_string)
for letter in count_list:
    count_letter = 0
    for letter_in_word in our_string:
        if letter == letter_in_word:
            count_letter += 1
    our_dict[letter] = count_letter
print(our_dict)           





