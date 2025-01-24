

username=input("Имя пользователя:")
title=input('Введите главный заголовок заметки:')
title1=input('Введите первый заголовок заметки:')
title2=input('Введите второй заголовок заметки:')
title_zar=[title,title1,title2]
content=input('Введите содержание:')
status=input('Введите статус:')
created_date=input('Введите дату создания заметки:')
issue_date=input('Введите дату истечения заметки:')

print('Имя пользователя',username)
print('Введите главный заголовок заметки:',title)
print("\nСписок заголовков:")
for title in title_zar:
    print(title)
print("Описание заметки:",content)
print("Статус заметки:",status)
print("Дата создания заметки:",created_date[0:8])
print("Дата истечения заметки:",issue_date[0:8])


