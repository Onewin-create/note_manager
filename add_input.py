
username=input("Имя пользователя:")
title=input('Введите главный заголовок заметки:')
content=input('Введите содержание:')
status=input('Введите статус:')
created_date=input('Введите дату создания заметки:')
issue_date=input('Введите дату истечения заметки:')

print('Имя пользователя',username)
print('Введите главный заголовок заметки:',title)
print("Описание заметки:",content)
print("Статус заметки:",status)
print("Дата создания заметки:",created_date[0:8])
print("Дата истечения заметки:",issue_date[0:8])


