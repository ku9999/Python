import datetime
an = ['Числитель','Знаменатель']
_,week_number,_ = datetime.datetime.now().isocalendar()
print(an[week_number%2])
