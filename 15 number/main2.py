for a in range(1,1000,1):
  k = 0
  for x in range(1,1000,1):
    if ((((x % a != 0) or (x % 375 != 0)) or (x % 100 == 0)) and (a > 10)) == 0:
      k = 1
    if k == 1:
      break
  if k == 0:
    print(a)
    break
