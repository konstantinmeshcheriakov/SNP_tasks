
from datetime import datetime, timedelta
def date_in_future(a = None):
    nowDate = datetime.now()
    if isinstance(a, int):
        newDate = nowDate + timedelta(days=a) 
        return newDate.strftime('%d-%m-%Y %H:%M:%S')
    else:
        return nowDate.strftime('%d-%m-%Y %H:%M:%S')

