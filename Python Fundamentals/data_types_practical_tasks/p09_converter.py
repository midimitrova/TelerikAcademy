import math

m = int(input())

mile = 1.6
km = 100 / mile

galon = 4.54
liters = 4.54 /m

result = math.floor(km * liters)

print(f'{result} litres per 100 km')