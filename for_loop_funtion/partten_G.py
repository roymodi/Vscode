def G():
    for row in range(0,6):
        for col in range(0,6):
            if (row==0 and col<5 or col==0)or(row==5 and col<5)or(row==3 and col>2)or(row==4 and col>3 and col<5):
                print("*",end="")
            else:
                print(end=' ')
        print()

G()