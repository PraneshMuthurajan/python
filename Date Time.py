import datetime
d=int(input("Type the date:  "))
m=int(input("Type the month:  "))
y=int(input("Type the year:  "))
answer=datetime.datetime(y, m, d)
print(answer.strftime("%A"))

