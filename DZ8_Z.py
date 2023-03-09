def edit_contact(contacts_file):
    edit_by = input('Введите контакт который надо изменить: ')
    if edit_by in contacts_file:
        edit = input ("Введите новый номер телефона: ")
        contacts_file[edit_by] = edit
        print(f"Контакт {edit_by} успешно изменен.")
    else:
        print(f"Контакт {edit_by} не найден в справочнике.")    