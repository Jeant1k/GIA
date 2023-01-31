f = open('27v11_B.txt')
n = int(f.readline())
mn = 1000000000000000
S = 0
d = 0
d51 = []
for i in range(n):
  a, b = map(int, f.readline().split())
  mn = a
  if b < a:
    mn = b
  S += mn
  d = abs(a - b)
  if d % 51 != 0:
    d51.append(d)
S += d51[0]
if S % 51 != 0:
  print('Молодец! ', S, S % 51)
else:
  print('Ищи давай его! ', S, S % 51, d)
