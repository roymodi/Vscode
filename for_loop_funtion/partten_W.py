def W():
    for row in range(0,3):
        for col in range(0,7):
            if (row==col)or (row==6-col)or col*row==3:
                print('*',end='')
            else:
                print(end=' ')
        print()
W()