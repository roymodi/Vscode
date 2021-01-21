def U():
    for row in range(0,5):
        for col in range(0,5):
            if (col==0 and row!=4)or(col!=0 and row==4 and col!=4)or(col==4 and row!=4) :
                print("*",end="")
            else:
                print(end=' ')
        print()

U()