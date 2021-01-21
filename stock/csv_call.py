import os

def file():  # find (.txt) file this funtion
    p=os.getcwd()
    f=os.listdir(p)
    for x in f:
        if (x.endswith(".csv"))==False:
            continue
        else:
            return x
