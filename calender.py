from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
import pandas as pd
import requests
import re
import time
import csv
import datetime
import os



chrome_options = Options()  
chrome_options.add_argument('--headless')  
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path=r"C:/Users/d'Angelo/Desktop/ETHstuff/Calender/chromedriver.exe")

driver.implicitly_wait(4)
driver.maximize_window()

driver.get('https://app.planning.nu/madurodam/madurodam-b.v./')
driver.find_element_by_name('xvalues[user]').send_keys('dangelo')
driver.find_element_by_name('xvalues[pass]').send_keys('')
driver.find_element_by_name('submit').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="main-nav"]/li[2]/a').click()
time.sleep(3)
#driver.get('https://app.planning.nu/madurodam/madurodam-b.v./rooster2/index2')

time.sleep(1)

# my_url = driver
# domain = urlparse(my_url).netloc

# response = requests.get(my_url)
# print("Status is", response.status_code)
# if response.status_code != 200:
# 	print("Can't scrape this!", response.status_code)
# else:
# 	print("Scraping...")
# 	html = response.text
# 	soup = BeautifulSoup(html, "html.parser")
# 	if domain in saved_domains:
# 		div_class = saved_domains[domain]
# 		body_ = soup.find("div", {"class": div_class})
# 	else:
# 		body_ = soup.find("body")
# 	words = body_.text.split()
# 	clean_words = clean_up_words(words)
# 	word_counts = counter(clean_words)
# #	print(word_counts.most_common(30))
# 	filename = datetime.date + '.csv'
# 	path = 'csv/' + filename
# 	if not os.path.exists(path):
# 		with open(filename, 'w') as csvfile:
# 			header_columns = ['', '', '']
# 			writer = csv.DictWriter(csvfile, fieldnames=header_columns)
# 			writer.writeheader()


# df = pandas.read_csv('rooster.csv', 
#             index_col='Employee', 
#             # parse_dates=['Hired'],
#             header=0, 
#             names=['Employee', 'Hired', 'Salary', 'Sick Days'])
# df.to_csv('rooster_modified.csv')

rooster = driver.find_elements_by_class_name("calender")

for div in rooster:
	filename = "C:/Users/d'Angelo/Desktop/ETHstuff/employee_file.csv"
	rooster.to_csv(filename, encoding='UTF-8')
	print(div.text,)

driver.close()
driver.quit()
print("Copy Complete")