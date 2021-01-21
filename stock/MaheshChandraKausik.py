from requests_html import HTMLSession
import datetime
import pandas as pd

def intraday(x):
    session=HTMLSession()
    snam=x.upper()
    web="https://in.finance.yahoo.com/quote/"+snam+".NS/history?p="+snam+".NS"
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

    # calculate 30 DMA 
    d50=df.iloc[1:51]
    cl50=d50['Close*']
    dmalist=[]
    for x in cl50:
        dmalist.append(float(x.replace(",","")))
    dma50=sum(dmalist)/len(dmalist) # this is 50 dma price
    tday=df.iloc[0]
    lday=df.iloc[1]
    
    lcp=float((lday['Close*']).replace(',','')) #last day close price
    lop=float((lday['Open']).replace(',','')) # last day open price
    ldv=lcp-lop # last day  close price-last day open price

    top=float((tday['Open']).replace(',','')) # today open price
    tdv=top-lcp # today open price - last day open price

# Chake last value (ldv) and today value(tdv) is '-' or '+'// lass then 0 or gether then 0
    if ldv<0 and tdv<0 and (float(liveP.replace(",","")) < dma50):
        post="Sell"
    elif (float(liveP.replace(",",""))==dma50):
        post=("Don't Buy or Sell in Intraday")
    else:
        post="Buy"

    return post,("LivePrice: ",liveP)

print(intraday(input("stock: ")))