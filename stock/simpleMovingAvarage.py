from requests_html import HTMLSession
import datetime
import pandas as pd



session = HTMLSession()
s_nm=input("stock: ")
stock=s_nm.upper()
web="https://in.finance.yahoo.com/quote/"+stock+".NS/history?p="+stock+".NS"
url = session.get(web)
liveP=url.html.find(".Fz\\(36px\\)",first=True).text
tab=url.html.find("table",first=True).text
table=tab.splitlines()

for x in table:
    if 'Dividend' in x:
        ind=table.index(x)
        table.remove(x)
        table.pop(ind-1)
hdlist=[]
mnlist=[]
ndlist=[]
hd=['Date', 'Open', 'High', 'Low', 'Close*', 'Adj. close**', 'Volume']

for x in table:
    ndlist.append(x)
    if len(ndlist)==7 and (ndlist==hd):
        hdlist.extend(ndlist.copy())
        ndlist.clear()
    elif len(ndlist)==7 and (ndlist!=hd):
        mnlist.append(ndlist.copy())
        ndlist.clear()
    else:
        pass


df=pd.DataFrame(mnlist,columns=hdlist)

SMA_50=df["Close*"].iloc[1:51]
sma_50=[]
for x in SMA_50:
    sma_50.append(float(x.replace(",","")))
sma50=round(sum(sma_50)/len(sma_50),2)

# def trand(l,v):
#     for x in l:
#         if v<x:
#             return True
#         else:
#             return False

# Trand=trand(sma_50,sma50)

SL=df["Close*"].iloc[1:22]
sl=[]
for x in SL:
    sl.append(float(x.replace(",","")))
slowline=round(sum(sl)/len(sl),2)


FL=df["Close*"].iloc[1:8]
fl=[]
for x in FL:
    fl.append(float(x.replace(",","")))
firstline=round(sum(fl)/len(fl),2)


if (slowline < firstline) and (sma50 < (float(liveP.replace(",","")))):
    print("buy",liveP)
else:
    print("Sell",liveP)
