def sch(start, x):
    if x < start:
        return 0
    if x == start:
        return 1
    return sch(start + 3, x) + sch(start * 3, x)


print(sch(3, 24) * sch(24, 68) * sch(70, 87))
