from selenium import webdriver
import time
import csv


s_nm=input("stock: ")
stock=s_nm.upper()
url="https://in.finance.yahoo.com/quote/"+stock+".NS/history?p="+stock+".NS"

#headless mode on
fire_option=webdriver.FirefoxOptions()
fire_option.add_argument("-headless")
#get url
driver=webdriver.Firefox(executable_path="geckodriver-v0.26.0-win64\\geckodriver.exe",options=fire_option)
driver.get(url)

# this is stock table header
hd=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table/thead/tr")
hdtx=hd.text
hl=hdtx.split()
z=hl.index("Adj.")
x1=hl.remove("Adj.")
x=hl.remove("close**")
y=hl.insert(z,"adj_close**")


# this is csv header create
file_name=stock+".csv"
try:
	with open(file_name,"x",newline="") as stock:
		write=csv.DictWriter(stock,hl)
		write.writeheader()

except:
	with open(file_name,"w",newline="")as stock:
		write=csv.DictWriter(stock,hl)
		write.writeheader()


#this is table history of stock
tb=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table/tbody")
tb1=tb.text
tb2=tb1.replace(',','')
tb3=tb2.splitlines() #this is list(tb3)
for x in tb3:
    if "Dividend" in x:
        tb3.remove(x)

# csv row table creat 
for x in tb3:
	lis2=x.split(" ")
	print(type(lis2))
	print(lis2)
	with open(file_name,"a",newline="") as stock:
		writerow=csv.writer(stock)
		writerow.writerow(lis2)



driver.quit()