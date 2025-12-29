# Разработать метод date_in_future(integer), который вернет дату через integer дней.
# Если integer не является целым числом, то метод должен вывести текущую дату.
# Формат возвращаемой методом даты должен иметь следующий вид '24-03-2001
# 22:33:44'.
# Тесты для примеров и проверки:
import datetime
import time
def date_in_future(a = None):
    day = time.localtime().tm_mday
    mon = time.localtime().tm_mon
    year = time.localtime().tm_year
    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min
    sec = time.localtime().tm_sec
    if a == None or type(a) != int:
        return f'{day}-{mon}-{year} {hour}:{minute}:{sec}' 
    # else:
    #     if mon == 
    #     return f'{day}-{mon}-{year} {hour}:{minute}:{sec}'  
print(date_in_future([])) # => текущая дата
print(date_in_future(2)) # => текущая дата + 2 дня
# print(datetime.strprime())

