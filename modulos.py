import math

import datetime

import random

import calendar

data_hora_atual = datetime.datetime.now()
data_formatada = data_hora_atual.strftime('%D/%m/%Y %H:%M:%S')


print(data_hora_atual)
print(data_formatada)
num = 4
print(math.sqrt(num))

print(random.random())

print(random.randint(1,100))

numeros = [1,2,3,4,5,6,7,8,9,10]

print(random.choice(numeros))

cal_octuber = calendar.month(2024,10)
print(cal_octuber)