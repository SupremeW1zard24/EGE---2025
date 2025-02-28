count = 0
for line in open("9.txt"):
    a = list(map(int, line.split()))
    s0 = sum(x for x in a if x % 2 == 0)
    s1 = sum(x for x in a if x % 2 != 1)
    if max(a) < sum(a) - max(a) and s0 == s1:
        count += 1
print(count)   # 11
