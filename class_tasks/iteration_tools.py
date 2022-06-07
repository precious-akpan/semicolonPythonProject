import itertools

for i, j in itertools.product(range(1, 13), range(1, 13)):
    print("{} x {} = {}".format(i, j, i*j))
    if j == 12:
        print()
