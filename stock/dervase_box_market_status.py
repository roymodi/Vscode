import os
import low_high as lh

# find (.txt) spacial tipe file in folder
def file():  # find (.txt) file this funtion
    p=os.getcwd()
    f=os.listdir(p)
    for x in f:
        if (x.endswith(".txt"))==False:
            continue
        else:
            return x

f=file()
with open(f,'r')as op:
    f=op.readlines()
    #f.reverse()
    h=[0]
    l=[0]
    for x in f:
        x=x.strip("\n")
        data=lh.low_high(x)
        hp=float(h[-1])-float(data[0])
        hl=float(l[-1])-float(data[1])
        h.append(data[0])
        l.append(data[1])
        print("______________________________________________________________________________________________")
        print(x," ",'high: ',data[0],' ',hp,'  ','low: ',data[1],' ',hl)
        if hp>0 and hl<0 :print("__STABLE__")
        elif hp<0 and hl>0:print("__STABLE__")
        elif hp>0 and hl>0: print('__DOWN__') 
        else:print("__UP__")

