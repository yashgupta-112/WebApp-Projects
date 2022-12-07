from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notify(title,message):
    notification.notify(
        title= title,
        message = message,
        timeout = 10
    )
def getdata(url):
    r=requests.get(url)
    return r.text

if __name__ == "__main__":
    while True:
        mydata=getdata('https://www.mohfw.gov.in/')

        soup =BeautifulSoup(mydata,'html.parser')
        mydatastr = ""
        for tr in soup.find_all('tbody')[1].find_all('tr'):
            mydatastr+= tr.get_text()
        mydatastr = mydatastr[1:]
        itemlist=mydatastr.split("\n\n")

        states =['Chandigarh','uttar Pardesh']
        for item in itemlist[0:22]:
          datalist = item.split()
          if datalist[1] in states:
              if datalist[1] in states:
                  ntitle ='cases'
                  ntext =f"state{datalist[1]}\n Indian : {datalist[2]}"
                  notify(ntitle,ntext)
                  time.sleep(2)
        time.sleep(10)
