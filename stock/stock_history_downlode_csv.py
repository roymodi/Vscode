from requests_html import HTMLSession
import time
import csv

session = HTMLSession()
s_nm=input("stock: ")
stock=s_nm.upper()
web="https://in.finance.yahoo.com/quote/"+stock+".NS/history?p="+stock+".NS"

url = session.get(web)
time.sleep(2)
tab=url.html.find("table",first=True).text
table=tab.splitlines()


for x in table:
    if 'Dividend' in x:
        ind=table.index(x)
        table.remove(x)
        a=table.pop(ind-1)
        
count=0
for x in table:
    _2nd_element=7*count
    _1st_element=_2nd_element-7
    if (_2nd_element>0 or _1st_element>7) and (_2nd_element<700 or _1st_element<707):
        line=(table[_1st_element:_2nd_element])
        file_name=stock+".csv"
        try:
            with open(file_name,'x',newline='')as file:
                rows=csv.writer(file)
                rows.writerow(line)
        except:
            with open(file_name,'a',newline='')as file:
                rows=csv.writer(file)
                rows.writerow(line)

    count=count+1