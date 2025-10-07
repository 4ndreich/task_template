def i():
    name = str('Артём')
    age = int(26)
    country = {'Россия': 'Новосибирск, Кировский район'}
    formatted_string = ','.join(f'{key}: {value}' for key, value in country.items())
    profession = str('polismen')
    print(f"\nВаше имя:'{name}'")
    print(f"\nВаш возраст:'{age}',\nСтрана проживания:'{formatted_string}',\nВаша проффесия:'{profession}'")


i()
