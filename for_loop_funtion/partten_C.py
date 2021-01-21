def C():
    for row in range(0,6):
        for col in range(0,5):
            if (row==0 and col!=0 or row==5 and col!=0)or (col==0 and row!=0 and row !=5):
                print('*',end='')
            else:
                print(end=' ')
        print()

C()