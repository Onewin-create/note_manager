


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
note['Введите дату истечения заметки:'] = issue_date
note['Заголовки: '] = title_list


print("\nЗаметка:")

for key, value in note.items():
        print(f"{key}: {value}")
