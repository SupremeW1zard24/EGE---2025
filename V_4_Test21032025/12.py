for n in range(1, 100):
    s = ">" + "0" * 17 + "3" * n + "2" * 17
    while ">3" in s or ">2" in s or ">0" in s:
        s = s.replace(">3", "22>", 1)
        s = s.replace(">2", "2>", 1)
        s = s.replace(">0", "3>", 1)
    sm = sum(map(int, s[:-1]))
    print(n, sm)  # 9 (по усл.)
