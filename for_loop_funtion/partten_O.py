def O():
    for row in range(0,6):
        for col in range(0,6):
            if (col!=0 and row==0 and col!=5)or(col!=0 and row==5 and col!=5)or(row!=0 and col==0 and row!=5)or(row!=0 and col==5 and row!=5):
                print('*',end='')
            else:
                print(end=" ")
        print()

O()