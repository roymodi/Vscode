def M():
    for row in range(0,6):
        for col in range(0,7):
            if (col==0 or col==6)or(row==col-1 and row<=2)or((col>=5-row and col<=5-row)and col>=3):
                print('*',end='')
            else:
                print(end=" ")
        print()

M()