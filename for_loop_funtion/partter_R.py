def R():
    for row in range(0,7):
        for col in range(0,6):
            if(col==0 or row==0 and col<5)or(row==3 and col<5)or(row>0 and col==5 and row<3)or(row-col==2):
                print("*",end="")
            else:
                print(end=' ')
        print()

R()