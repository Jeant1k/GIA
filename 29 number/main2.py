f = open('27-29b.txt')
n = int(f.readline())
Summ = 0
dmin = 100000
for s in f:
  a = list(map(int, s.split()))
  a.sort()
  Summ += a[1] + a[2]
  if a[1] - a[0] < dmin and a[1] - a[0] % 5 != 0:
    dmin = a[1] - a[0]
print(Summ - dmin, (Summ - dmin) % 5)
