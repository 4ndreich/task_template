 
phone_models = [ 
 "iPhone 15", 
 "Samsung Galaxy S23", 
 "Google Pixel 8", 
 "Xiaomi 14", 
 "OnePlus 12", 
 "Huawei P60", 
 "Realme GT 3", 
 "Nothing Phone 2", 
 "Sony Xperia 1 V", 
 "Motorola Edge 40" 
] 

print(f"Всего доступно моделей: {len(phone_models)}") 
 
try: 
    choice = int(input("\nВведите номер модели, которую хотите получить в подарок (1-10): ")) 
 
    if 1 <= choice <= len(phone_models): 
     print(f"\nПоздравляем! Вы получаете: {phone_models[choice - 1]}") 
    else: 
     print("\nОшибка: такого номера нет в списке!") 
except ValueError: 
    print("\nОшибка: введите целое число!") 

delivery_city = {
    "Россия": ["Москва", "Санкт-Петербург", "Новосибирск",],
    "Украина": ["Харьков", "Киев", "Караганда",],
    "Беларусь": ["Минск", "Гомель", "Гродно"]
}

print("\nДоступные страны доставки:")
countries = list(delivery_city.keys())
for i, country in enumerate(countries, 1):
        print(f"{i}. {country}")
    
country_choice = int(input("\nВыберите страну доставки (1-3): "))
if country_choice < 1 or country_choice > len(countries):
        print("Ошибка: выбран неверный номер страны.")
        exit()
    

selected_country = countries[country_choice-1]
cities = delivery_city[selected_country]
    
print(f"\nДоступные города в {selected_country}:")
for i, city in enumerate(cities, 1):
        print(f"{i}. {city}")
    
city_choice = int(input("\nВыберите город доставки (1-3): "))
if city_choice < 1 or city_choice > len(cities):
        print("Ошибка: выбран неверный номер города.")
        exit()
 
selected_phone = phone_models[choice-1]
selected_city = cities[city_choice-1]
    

print(f" Поздравляем! Вы получаете в подарок: {selected_phone}")
print(f" Доставка будет осуществлена в: {selected_city}, {selected_country}")


    
