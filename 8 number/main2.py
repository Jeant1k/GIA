from itertools import product

alphabet = "ЕГЭ"
count = 0;

for i in product(alphabet, repeat = 5):
    if i[0] == 'Е' or i[0] == 'Э':
        count += 1;
print(count)
