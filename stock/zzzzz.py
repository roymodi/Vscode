from requests_html import HTMLSession
import pandas as pd 

session=HTMLSession()
a=session.get('https://www.nseindia.com/api/historical/cm/equity?symbol=ITC&series=["EQ"]&from=30-06-2020&to=25-08-2020&csv=true',stream=True)
table=(a.text).splitlines()

hli=[]
bdli=[]
he=['ï»¿', 'Date', 'series', 'OPEN', 'HIGH', 'LOW', 'PREV.CLOSE', 'ltp', 'close', 'vwap', '52WH', '52WL', 'VOLUME', 'VALUE', 'Nooftrades']
for x in table:
    y=(((x.replace(" ","")).replace(',','')).replace('"',' ')).split(" ")
    z=' '.join(y).split() # empity string remove 
    if z==he:
        hli.extend(z[1:15])
        
    elif z!=he:
        bdli.append(z)
        
df=pd.DataFrame(bdli,columns=hli)

print(df)

# l=(df['close'].iloc[0:7])
# lis=[]
# for x in l:
#     lis.append(x)
# print(lis)