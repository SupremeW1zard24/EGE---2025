num = 0
for line in open("9.txt"):
    num += 1
    a = list(map(int, line.split()))
    if a == sorted(a) and any(sum(map(int, str(x))) % 2 == 0 for x in a if a.count(x) > 1):
        print(num)  # 6937
