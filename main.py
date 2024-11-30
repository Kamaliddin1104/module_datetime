from datetime import date

today = date.today()
print(f"Сегодня : {today}") # Показывает сегодняшнюю дату

# Методы
day = today.day # Сегодняшнее число
month = today.month # Нынешний месяц
year = today.year # Нынешний год


# Как напечатать дату в формате: Четверг 12 Декабрь 2024
print(today.strftime("%A, Число: %d %B, Год: %Y"))
