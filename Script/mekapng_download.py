#from selenium import webdriver
import time
from bs4 import BeautifulSoup
from urllib import request


google_url = 'lh3.googleusercontent.com'

png_file = open('UrlList1-297.txt','r')

for i in range(1,447):

    url_meka = png_file.readline()

    if google_url in url_meka:
        
        num = i
        data = request.urlopen(url_meka).read()
        image = open('./' + '%d' %num + ".png",'wb')
        image.write(data)
        image.close()

png_file.close()
    
    