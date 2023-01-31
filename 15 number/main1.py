for a in range(-1000, 1000):
  k = 1
  for x in range(1000):
    for y in range(1000):
      if ((y + 5 * x <= 34) <= ((y - x > 4) or (y <= a))) == 0:
        k = 0
      if k == 0:
        break
    if k == 0:
      break
  if k == 1:
    print(a)
    break
