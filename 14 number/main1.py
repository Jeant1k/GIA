S = 3 ** 2017 + 9 ** 1000 - 27
k = 0
while S > 0:
  if S % 3 == 2:
    k += 1
  S //= 3
print(k)
