for i in range(100000):
    s = i
    n = 0
    while s < 85:
        s += 4
        n += 11
    if n == 242:
        print(i)
