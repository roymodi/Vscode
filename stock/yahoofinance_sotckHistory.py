import pandas as pd
import requests


a=requests.get("https://query1.finance.yahoo.com/v7/finance/download/SBIN.NS?period1=1564632664&period2=1596255064&interval=1d&events=history",stream=True)
table=(str(a.text)).splitlines()


head=[]
main=[]
for x in table:
    if (x.split(","))==['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']:
        head.extend((x.split(",")))
    elif (x.split(","))!=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']:
        main.append((x.split(",")))
    else:
        pass
df=pd.DataFrame(main,columns=head)
print(df['Open'])
