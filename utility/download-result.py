#!/usr/bin/python

from bs4 import BeautifulSoup as bs
import selenium.webdriver as webdriver
import requests
import json
import io
import os

file = "/resources/raceday_2017.json"
new_folder = "/raw/2017/result/"

print ('Scraping raceday data.')
print ('Processing ...')

current_path = os.getcwd()
os.chdir("..")
root_path = os.getcwd()
target_path = root_path + file

if not os.path.exists(root_path + new_folder):
	os.makedirs(root_path + new_folder)

with open(target_path) as fp:
	dictdump = json.loads(fp.read())

for date in dictdump["date"]:
	target_url = 'http://hk.racing.nextmedia.com/results.php?date=' + date
	driver = webdriver.PhantomJS(executable_path=r'/Users/garychan/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
	driver.get(target_url)
	data = driver.page_source
	filename = root_path + new_folder + date + ".html"
	with io.open(filename,'w',encoding="utf-8") as outfile:
		outfile.write(unicode(data))
	print "saved " + date + "."

print ('Done.')