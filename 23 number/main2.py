def May4(start, x):
  if x < start:
    return 0
  if x == start:
    return 1
  K = May4(start + 1, x) + May4(start + 2, x) + May4(start + 4, x)
  return K

print(May4(21, 30))
