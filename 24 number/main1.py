k = 1
mx = 0
with open('24.txt') as f:
  D = f.read()
  for i in range(len(D) - 1):
    if D[i] <= D[i + 1]:
      k += 1
    else:
      if k > mx:
        mx = k
      k = 1
print(mx)
