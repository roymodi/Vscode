def Z():
    for row in range(0,5):
        for col in range(0,5):
            if row==0 or row==4 or row==4-col:
                print('*',end="")
            else:
                print(end=' ')
        print()
Z()