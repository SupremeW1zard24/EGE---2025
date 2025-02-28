from string import *

alpha = (digits + ascii_uppercase)[:24]
for x in alpha:
    n = int(f"12{x}734", 24) + int(f"8{x}95{x}3", 24) + int(f"24{x}796", 24)
    if n % 23 == 0:
        print(n // 23)
