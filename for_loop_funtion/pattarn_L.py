def L():
    for row in range(0,5):
        for col in range(0,5):
            if col==0 or row ==4 :
                print("*",end="")
            else:
                print(end=' ')
        print()

L()