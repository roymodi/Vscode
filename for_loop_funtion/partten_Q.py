def Q():
    for row in range(0,7):
        for col in range(0,7):
            if (col!=0 and row==0 and col<5)or(row!=0 and col==0 and row<5)or(col!=0 and row==5 and col!=6)or(row!=0 and col==5 and row!=6)or(row>=3 and row==col):
                print('*',end='')
            else:
                print(end=" ")
        print()

Q()