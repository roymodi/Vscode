import csv

def Low(x):
    with open(x,"r")as low:
        file=csv.DictReader(low)
        value=[]
        for x in file:
            l=x.get("Low")
            value.append(l)
        low=min(value)
        return low

def High(x):
    with open(x,"r")as low:
        file=csv.DictReader(low)
        value=[]
        for x in file:
            l=x.get("High")
            value.append(l)
        high=max(value)
        return high

def low_high(x):
    h=High(x)
    l=Low(x)
    return h,l



