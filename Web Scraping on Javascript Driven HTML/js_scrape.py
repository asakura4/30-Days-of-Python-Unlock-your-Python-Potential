import requests
import os
import shutil
from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = "https://www.chrisburkard.com/Shop/Best-Sellers"
web_r = requests.get(url)
web_soup = BeautifulSoup(web_r.text, 'html.parser')

#print(web_soup.findAll("img"))
#<img src=''/?

driver = webdriver.Chrome()
driver.get(url)


iterations = 0
while iterations < 10:
	html = driver.execute_script("return document.documentElement.outerHTML")
	sel_soup= BeautifulSoup(html, 'html.parser')
	print(len(sel_soup.findAll("img")))
	images =[]
	for i in sel_soup.findAll("img"):
		print(i)
		src = i["src"]
		images.append(src)
	print(images)
	current_path = os.getcwd()
	for img in images:
		try:
			file_name = os.path.basename(img)
			img_r = requests.get(img, stream=True)
			new_path = os.path.join(current_path, "images", file_name)
			with open(new_path,"wb") as output_file:
				shutil.copyfileobj(img_r.raw, output_file)
			del img_r
		except:
			pass

	iterations += 1
	time.sleep(1)