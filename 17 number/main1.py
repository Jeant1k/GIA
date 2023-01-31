k = 0
mx = 0
for i in range(2050, 80392):
  if i % 10 == 2 or i % 10 == 7:
    if i % 3 == 0 and i % 7 == 0 and i % 11 == 0:
      k += 1
      if i > mx:
        mx = i

print(k, mx)
