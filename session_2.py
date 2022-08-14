def hello():
    print('hii')


hello()

name = input('name')
print('So, your name is {}'.format(name))
name_array = list(name)

age = input('age')

from math import sqrt
import datetime as dt

x = sqrt(100)
print(x)



now_is = dt.datetime.now()
now_is.strftime("%A")

for number in range(0,20,2):
    print(dt.datetime.now())

def hello():
    print('hii')

hello()
