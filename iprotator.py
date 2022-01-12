import json 
from playwright.sync_api import sync_playwright 
import refractor
import os
from bs4 import BeautifulSoup
 
file = open("proxy.txt","w",encoding='utf-8')
#url = input("Enter url to scrape from: ")
url = "https://www.pexels.com/search/"
cat = input("Search category: ")
url = url+cat+"/"
print(url)
with sync_playwright() as p: 
    for browser_type in [p.firefox]:
        browser = browser_type.launch() 
        page = browser.new_page() 
        page.goto(url)
        print("writing contents: ")
        #soup = BeautifulSoup(page.content(),'html.parser')
        file.writelines(str(page.content()))       
        browser.close() 

       
file.close()
print("Finished writing contents: ")
#os.system('./curling.sh')
#refractor.filter()

#jsonContent = json.loads(page.inner_text('pre')) 
        #print(page.content()) 
        #, p.webkit]: p.chromium,