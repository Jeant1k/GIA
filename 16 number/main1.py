def F(n):
  if n == 1:
    return 1
  if n == 2:
    return 2
  if n > 2 and n % 2 == 0:
    return ((7 * n + F(n - 3)) / 9) // 1
  if n > 2 and n % 2 != 0:
    return ((5 * n + F(n - 1) + F(n - 2)) / 7) // 1

print(F(50))
