from requests_html import HTMLSession
import time

def main(x): # x is stock name
    session = HTMLSession()
    stock=x.upper()
    web="https://in.finance.yahoo.com/quote/"+stock+".NS/history?p="+stock+".NS"

    url = session.get(web)
    css1=".Fz\\(36px\\)"
    css2='span.Trsdu\\(0\\.3s\\):nth-child(2)'
    css3='#quote-market-notice'
    price=url.html.find(css1,first=True).text
    ratio=url.html.find(css2,first=True).text
    merket_status=url.html.find(css3,first=True).text
    return price,ratio,merket_status

def stock_live(x):
    while True:
        time.sleep(15)
        p=main(x)
        c=p[2].split()
        if c[1]=="close:":
            break
    return p

# x=input('stock: ')
# print(stock_live(x))
    
