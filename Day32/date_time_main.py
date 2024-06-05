import datetime as dt

now = dt.datetime.now()
year = now.year  # also contains date month hour minute weekday ...
day_of_week = now.weekday()
print(type(now))

date_of_birth  =  dt.datetime(2001, 2,23)
print(date_of_birth)