for i in range(1, 10000):
  x = i
  L = 0
  M = 0
  while x > 0:
    M += 1
    if x % 8 > 4:
      L += (x % 8)
    x //= 8
  if L == 12 and M == 4:
    print(i)
