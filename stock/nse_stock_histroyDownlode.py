from datetime import date
import datetime
from nsepy import get_history
import pandas as pd

x=datetime.datetime.now() #today date and time in int type
tdy=x.year #today year int type
tdm=x.month #today month int type
tdd=int(x.day)-1 #today day int type(-1 for yesterday)

#change year 
s=str(x).split()
today=(str(s[0]).replace('-',',')) # today date in str type
cyr=int(x.year)-3 # year last 3 year
change_date=today.replace((str(x.year)),str(cyr)).split(',')#change date in str type

cdy=int(change_date[0])# change year int type
cdm=int((change_date[1]))# change month int type
cdd=int(change_date[2])# change day int type


# stock name convert upper case
s_nm=input("stock: ")
stock=s_nm.upper()

# creat file name csv file
file_name=stock+".csv"

# nsepy module from stock history downlode .csv file 
stock_dataframe = get_history(symbol=stock,
                   start=date(cdy,cdm,cdd),
                   end=date(tdy,tdm,tdd))

stock_dict=dict(stock_dataframe)
dataframe=pd.DataFrame(stock_dict)
dataframe.to_csv(file_name)