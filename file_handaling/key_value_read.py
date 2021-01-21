import random

file=open('file_handaling\\new_2.txt','r')
r=file.readlines()
l=input('user: ')
for x in r:
    b=x.replace('\n','')
    y=b.split(':')
    a=l
    key=y[0]
    value=y[1]
    if a in key :
        print(value)
        #print(type(line))


file.close()