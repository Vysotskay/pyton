# Напишите программу для печати всех уникальных значений в словаре.
# {
#     1: 'Vlad',
#     2: 'Vlad',
#     3: 'Oleg'
# }
# -> 2

my_dictionary = \
    {
        "1": "Vlad",
        "2": "Vlad",
        "3": "Oleg "
    }
my_set = set()
for i in my_dictionary.values():
    my_set.add(i)    
print(my_set)    