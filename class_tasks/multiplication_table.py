for i in range(1, 13):
    print("{:2d} Multiplication Table:".format(i))
    for j in range(1, 13):
        print('{:3d} x {:2d} = {:3d}'.format(i, j, i * j))
    print()
