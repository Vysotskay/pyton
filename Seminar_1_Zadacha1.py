#1. За день машина проезжает n киллометров. Сколько дней нужно,чтобы проехать маршрут
 #длиной m киллометров? При решении этой задачи нельзя пользоваться условной инструкцией 
 #if и циклами.
 #**Input:**
 #n = 700
 #m = 750
 #**Output:**   #2


# n = 700
# m = 750
# day = int(m / n) + int(m // n)
# print(day)



# n = 700
# m = 750
# n = int(input())
# m = int(input())
# print((m + n - 1) // n)


import math
n = 700
m = 750
day = math.ceil(m / n)
print(day)