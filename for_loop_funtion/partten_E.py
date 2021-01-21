def E():
    for row in range(0,5):
        for col in range(0,4):
            if (row==0 or row==4 or col==0)or (row==2 and col!=3):
                print("*",end="")
            else:
                print(end=' ')
        print()

E()