S = 7 * 1296 ** 57 - 8 * 216 ** 30 + 35
k = 0
while S > 0:
  if S % 6 == 5:
    k += 1
  S //= 6
print(k)
