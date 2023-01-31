from itertools import product

alphabet = 'AOY'
count = 1

for i in product(alphabet, repeat = 5):
    if count == 210:
        print(''.join(i))
    count += 1
