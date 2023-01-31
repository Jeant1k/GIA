k = 0
mx = 0
with open('24-j7.txt') as f:
  S = f.read()
  for i in range(len(S) - 2):
    if int(S[i]) % 2 == 0:
      if int(S[i + 1]) % 2 == 0:
        k += 1
      else:
        if k > mx:
          mx = k
        k = 1
    else:
      if int(S[i + 1]) % 2 != 0:
        k += 1
      else:
        if k > mx:
          mx = k
        k = 1 
print(mx)
