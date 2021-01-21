from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

path="geckodriver-v0.26.0-win64\\geckodriver.exe"
url="https://"+(input("https:// "))

# this headless browser
firefox_option=Options()
firefox_option.add_argument("--headless")

#make driver path and headless
driver=webdriver.Firefox(executable_path=path,options=firefox_option)
driver.get(url)# input url

table=driver.find_element_by_tag_name("tbody")
cell=table.find_element_by_tag_name('tr')

print(cell)

driver.quit()