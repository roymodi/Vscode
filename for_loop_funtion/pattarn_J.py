def J():
    for row in range(0,7):
        for col in range(0,6):
            if row==0 or col==3 or row==6 and col<=3 or row==5 and col <=0:
                print('*',end='')
            else:
                print(end=' ')
        print()

J()