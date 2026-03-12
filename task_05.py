
from datetime import datetime, timedelta
def date_in_future(a = None):
    nowDate = datetime.now()
    if type(a) == int:
        newDate = nowDate + timedelta(days=a) 
        return f'{newDate.day}-{newDate.month}-{newDate.year} {newDate.hour}:{newDate.minute}:{newDate.second}'
    else:
        return f'{nowDate.day}-{nowDate.month}-{nowDate.year} {nowDate.hour}:{nowDate.minute}:{nowDate.second}'

