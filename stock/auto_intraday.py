import os
import csv
import intraday
import time

def stocks():
    path=os.getcwd()
    file=path+'\\'+'Nse_listed_company_name.csv'
    stocks=[]
    company=[]
    Market_Capitalisation=[]
    with open(file,'r')as op:
        slist=csv.DictReader(op)
        for x in slist:
            stocks.append(x['Symbol'])
            company.append(x['Company Name'])
            Market_Capitalisation.append(x['Market Capitalisation in Lakh'])
    return stocks,company,Market_Capitalisation

data_tuple=stocks()
stock_list=data_tuple[0]
company_name=data_tuple[1]
lenth=(len(stock_list))-1
c=0
while c<=lenth:
    time.sleep(5)
    stock=stock_list[c]
    company=company_name[c]
    
    try:
        data=intraday.intraday(stock)
        sd=stock+str(data)+"\n"
    except:
        pass
    ad=((str(data[0])).split())[0]
    if ad=="('Buy',":
        with open("Intraday_Buy.csv",'a')as op:
            op.write(sd)
    else:
        with open("Intraday_Sell.csv",'a')as op:
            op.write(sd)
    c+=1
