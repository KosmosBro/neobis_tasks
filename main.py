import json

print('\n', "Здравствуйте , вас приветствует программа 'KOSMOS' '\n")
print("Пожалуйста, выберете действие  ")

while True:
    print('_________________________________________')
    print('1 - записать нового студента.')
    print('2 - выйти из программы.')

    choise = input('выберете действие : ')

    if choise == '1':
        name = input('Введите имя : ')
        surname = input('Введите фамилию : ')
        midle_name = input('Введите отчество : ')
        age = input('Введите год рождения : ')
        month = input('Введите месяц рождения : ')
        day = input('Введите день рождения : ')
        faculty = input('Введите факультет : ')

        new_list = {
            'Name': name,
            'Lastname': surname,
            'Midlename': midle_name,
            'Age': age,
            'Month': month,
            'Day': day,
            'Faculty': faculty
        }

        with open(name + '.json', 'w') as f:
            stroka = json.dumps(new_list)
            print(stroka + '\n')
            f.write(stroka)

    elif choise == '2':
        break
