from datetime import datetime

a = datetime.strptime('2021 04 24 09 00 00','%Y %m %d %H %M %S')

b = datetime.now()

c = b-a

print(c)