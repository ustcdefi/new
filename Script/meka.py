from selenium import webdriver
import time
from bs4 import BeautifulSoup
from urllib import request


def page_info(number):

    chrome_driver = 'C:/Users/fcyj2/node_modules/chromedriver/lib/chromedriver/chromedriver.exe'
    b = webdriver.Chrome(executable_path = chrome_driver)
    b.get('https://opensea.io/assets/0x9a534628b4062e123ce7ee2222ec20b86e16ca8f/'+ '%d' %number )

    html_text = b.page_source
    time.sleep(0.5)
    b.quit()
    return html_text



    
    



if __name__ == '__main__':


    file_meka = open('UrlList.txt','a+')

    for i in range(298,8888):
        
        print(i)


        html_text = page_info(i)
    
        soup_page = BeautifulSoup(html_text,"html.parser")
    
        url_image = soup_page.find("meta",attrs={"property":"og:image"})
        

        
        
        #print(str(url_image))
        #print(url_image.text)

        file_meka.write(url_image.get('content'))
        file_meka.write('\n')

        # data = request.urlopen(url_image.get('content')).read()
        # image = open('./' + '%d' %i + ".png",'wb')
        # image.write(data)
        # image.close()
    
    file_meka.close()

        



    