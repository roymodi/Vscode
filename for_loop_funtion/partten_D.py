def D():
    for row in range(0,6):
        for col in range(0,5):
            if (row==0 and col!=4 or col==0)or(row==5 and col!=4)or(row !=0 and col ==4 and row !=5):
                print("*",end="")
            else:
                print(end=' ')
        print()

D()