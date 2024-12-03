from datetime import date, datetime, time

today = date.today() # Сегодняшняя дата
print(f"Сегодня : {today}") # Показывает сегодняшнюю дату

# Методы
day = today.day # Сегодняшнее число
month = today.month # Нынешний месяц
year = today.year # Нынешний год


# Как напечатать дату в формате: Четверг 12 Декабрь 2024
print(today.strftime("%A, Число: %d %B, Год: %Y"))

# След.год
next_year = today.replace(year = today.year + 1)
print(next_year)

difference = abs(next_year - today)
print(difference)


# ДР Никола Тесла
nicola = date(1856, 7, 10)
print(f"Др Николы: {nicola}")

week = nicola.weekday() # Выведет день недели в числах: 0 - Пон. 6 - Воскресенье
week_str_format = nicola.strftime("%A") # Форматирование дня недели в строку
print(f"{week}, {week_str_format}") # Outputs: 3


# class - Datetime
now = datetime.now() # Нынешнее дата и время
print(now)

date = now.date() # Год-Месяц-Число
print(f"Год: {now.year}, Месяц: {now.month}, Число: {now.day}, "
      f"День-недели: {now.strftime("%A")}, Час: {now.hour}, "
      f"Минута: {now.minute}, Секунды: {now.second}")



chernobyl = datetime.fromisoformat("1986-04-26 01:23:40.000+04:00")
print(f"Катастрофа в Чернобыле: {chernobyl}") # Числовые значения

print(chernobyl.strftime("День недели: %A, Месяц: %B, Число: %dth, Год: %Y, Время: %X")) # Форматирование в строку
print(f"Часовой пояс: {chernobyl.tzinfo}") # Часовой пояс



# Время - time()
my_time = time(12, 9, 9) # Час-минута-секунда
my_time_format = time.fromisoformat("12:09:09")
print(my_time_format)
print(my_time.strftime("%I:%M %p")) # Форматирование с am, pm



my_date = date.fromisoformat("2025-04-11")
my_bd = datetime.combine(my_date, my_time) # Объединение даты и времени
print(my_bd)