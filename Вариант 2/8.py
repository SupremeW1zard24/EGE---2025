from itertools import *

count = 0
for x in product("ЛЮСТРА", repeat=5):
    if x.count("Ю") <= 2 and x[-1] not in "ЛСТР":
        count += 1

print(count)
