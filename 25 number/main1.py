from math import sqrt

def xd(n):
  q = int(sqrt(n)) + 1
  div = []
  for i in range(2, q):
    if n % i == 0:
      if i == n // i:
        div.append(i)
      else:
        div.append(i)
        div.append(n // i)
  return div

for i in range(550001, 555000):
  D = xd(i)
  S = 0
  if len(D) > 0:
    for j in range(len(D)):
      if len(xd(D[j])) == 0:
        S += D[j]
  if S % 10 == 1:
    print(i, S)
