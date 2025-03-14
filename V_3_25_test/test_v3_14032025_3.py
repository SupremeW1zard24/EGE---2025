#1-25
#2-adbc
#3-1104600
#4-25

#5-113
def cc3(x):
    s = ""
    while x > 0:
        s = str(x % 3) + s
        x //= 3
    return s


def sum_dg(t):
    k = 0
    for el in str(t):
        k += int(el)
    return k


d = []

for n in range(1, 100):
    c3 = cc3(n)
    sm_dg = sum_dg(c3)
    if sm_dg % 2 == 0:
        c3 = "1" + c3 + "2"
    else:
        c3 = "2" + c3 + "0"
    r = int(c3, 3)
    if r > 100:
        d.append(r)

print(min(d))

#6-2418
#7-364605469
#8-1776


#9-44
f = open("9.txt")

count = 0
for el in f:
    a = [int(x) for x in el.split()]
    povtor = []
    nepovtor = []

    sum_pl = 0
    sum_mn = 0
    for x in a:
        if a.count(x) == 2:
            povtor.append(x)
        if a.count(x) == 1:
            nepovtor.append(x)
        if x > 0:
            sum_pl += x
        else:
            sum_mn += x

    if len(povtor) == 2 and len(nepovtor) == 4:
        if abs(sum_mn) > sum_pl:
            count += 1
print(count)


#10-11
#11-78 [16 * 4992 / 1024]
#12-8
#13-224


#14-3126
def cc5(n):
    a = []
    while n > 0:
        a.append(n % 5)
        n //= 5
    return a


for x in range(1, 5556):
    v = cc5(5 ** 150 + 5 ** 135 - x)
    if v.count(4) == 134:
        print(x)


#15-


#16-1
from functools import lru_cache


@lru_cache(None)
def f(n):
    if n >= 2010:
        return n
    return f(n + 3) + f(n + 2) + f(n + 1)


print((f(2000) - 2 * (f(2002) + f(2003))) / f(2004))

#22-10
