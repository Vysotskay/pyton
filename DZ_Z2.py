# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов 
# в массиве. В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 6
# -> 5
import sys
a=list(map(int,input().split()))
b=int(input())
c=[]
for i in a:
    c.append(b-i)
for i in a:
    if i==b:
        print(b)
        sys.exit()
if min(c)<0:
    d=c.index(max(c))
    print(a[d])
else:
    d=c.index(min(c))
    print(a[d])