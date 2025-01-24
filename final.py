
#username - имя пользователя
#title - заголовок заметки
#content - описание заметки
#status - статус заметки
#created_date - дата создания заметки в формате "день-месяц-год", например "10-11-2024"
#issue_date - дата истечения заметки (дедлайн) в формате "день-месяц-год", например "10-12-2024"


username=input("Имя пользователя:")
title=input('Введите главный заголовок заметки:')
title1=input('Введите первый заголовок заметки:')
title2=input('Введите второй заголовок заметки:')
content=input('Введите содержание:')
status=input('Введите статус:')
created_date=input('Введите дату создания заметки:')
issue_date=input('Введите дату истечения заметки:')
title_list=[title,title1,title2]


note = {}
note['Имя пользователя: '] = username
note['Описание заметки: '] = content
note['Статус заметки: '] = status
note['Дата создания заметки: '] = created_date
note['Дата истечения заметки (дедлайн): '] = issue_date
note['Заголовки: '] = title_list


print("\nЗаметка:")

for title in title_list:
    print(title)
