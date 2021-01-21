def V():
    for row in range(0,4):
        for col in range(0,7):
            if (row==col)or(row==6-col):
                print('*',end='')
            else:
                print(end=' ')
        print()
V()