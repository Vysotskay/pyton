# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# -Программа должна выводить данные
# -Программа должна сохранять данные в
# текстовом файле
# -Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# -Использование функций. Ваша программа
# не должна быть линейной
# 1.Вывод всех контактов
# 2.Поиск контакта
# 3.Добавить контакт(сразу сохранять в файл)
# 4.Выход по требованию пользователя

def all_contacts():
    with open('phone_number.txt', 'r', encoding='utf8') as data:
        for line in data:
            print(line)

# all_contacts()        
def find_contact(name):
    with open('phone_number.txt', 'r', encoding='utf8') as data:
        for line in data:
            if name in line:
                print(line)
find_contact('Иван')    

def add_contact(new_contact):
    with open('phone_number.txt', 'a', encoding='utf8') as data:
        data.write('new_contact')

def main_menu(numb):
    if numb == 1:
        all_contacts()
    elif numb == 2:
        name = input('Введите искомое имя: ')
        find_contact(name)
    elif numb == 3:
        data = input('Введите новый контакт')
        add_contact(data) 
numb = int(input('Введите 1 - для печати всего справочника; 2 - для поиска контакта; 3 - для записи контакта'))
main_menu(numb)               

