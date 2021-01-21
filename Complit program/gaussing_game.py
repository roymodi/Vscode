import random as rd

a=rd.randint(0,11)
left=3
while left > 0 :
    gase=int(input('gase the number: '))
    if (a==gase):
        print("you Win")
        break
    left=left-1
else:
    print("GameOver")