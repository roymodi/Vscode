from selenium import webdriver
import time

s_nm=input("stock: ")
stock=s_nm.upper()
url="https://in.finance.yahoo.com/quote/"+stock+".NS/history?p="+stock+".NS"

options=webdriver.FirefoxOptions()
options.add_argument("-headlesps")
driver=webdriver.Firefox(executable_path="geckodriver-v0.26.0-win64\\geckodriver.exe",options=options)
driver.get(url)

#this is live stock price
while True:  # get live data of stock
    time.sleep(2)
    live=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/div/div[3]/div/div/span[1]")
    print(live.text)


# # this is stock table header
# hd=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table/thead/tr")
# hdtx=hd.text
# hl=hdtx.split()
# z=hl.index("Adj.")
# x1=hl.remove("Adj.")
# x=hl.remove("close**")
# y=hl.insert(z,"adj_close**")
# hds=str(hl).strip("[]")
# print(hds)


# #this is table history of stock
# tb=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table/tbody")
# tb1=tb.text
# tb2=tb1.replace(',','')
# tb3=tb2.splitlines()
# for x in tb3:
#     if "Dividend" in x:
#         tb3.remove(x)
# for y in tb3:
#     print(y)


driver.quit()