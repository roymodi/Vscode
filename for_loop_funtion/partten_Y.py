def Y():
    for row in range(0,7):
        for col in range(0,7):
            if (row==col and row<4)or(row==6-col and row<4)or(col==3 and row>2):
                print('*',end='')
            else:
                print(end=' ')
        print()

Y()