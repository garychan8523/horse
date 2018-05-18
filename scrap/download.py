#!/usr/bin/python

from bs4 import BeautifulSoup as bs
import selenium.webdriver as webdriver
import requests
import json
import io

print ('Scraping all event date.')
print ('Processing ...')

#target_url = 'http://hk.racing.nextmedia.com/results.php?date=20170903'
target_url = 'http://hk.racing.nextmedia.com/oldfullresult.php'
driver = webdriver.PhantomJS(executable_path=r'/Users/garychan/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
driver.get(target_url)
#result  = requests.get(target_url)
#data = result.text
data = driver.page_source
soup = bs(data, "lxml")

out = soup.find('select', {'name': 'redirect'})
#out = soup.findAll('select')[1]
out = out.select('option')

obj = {'date': []}

for option in out:
	if('results.php' in option.attrs['value']):
		obj['date'].append(option.attrs['value'])


with io.open("all-date-old.json",'w',encoding="utf-8") as outfile:
	outfile.write(unicode(json.dumps(obj, ensure_ascii=False, indent=4)))

print ('Done.')