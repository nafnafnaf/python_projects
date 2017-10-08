
import sys, time, telepot, unicodedata, urllib3, wikiquote, random
from telepot.loop import MessageLoop
from urllib.request import urlopen, Request #as uReq
from bs4 import BeautifulSoup as soup
from tabulate import tabulate
#BeautifulSoup + Wikiquote part
def scrap():
    url = 'http://www.meteokav.gr/weather/'
    req = urlopen(url)
    page = req.read()
    req.close()
    page_soup = soup(page, "html.parser")
    containers = 'Θερμοκρασία: ' + page_soup.find("span", {"id":"ajaxtemp"}).text.strip()
    containers0 = 'Αίσθηση σαν: ' + page_soup.find("span", {"id":"ajaxfeelslike"}).text.strip()
    containers1 = 'Διαφορά 24ώρου: '+ page_soup.find_all("strong")[0].text.strip()
    containers2 = 'Διαφορά ώρας: '+ page_soup.find("td", {"rowspan":"5"}).find("td", {"class":"data1"}).text.strip() + page_soup.find_all("strong")[1].text.strip() #Διαφορά ωρας
    containers3 = page_soup.find_all("strong")[19].text.strip() + " " + page_soup.find("span", {"id":"ajaxhumidity"}).text.strip()#'Υγρασία: 
    containers4 = 'Ανεμος: ' + page_soup.find("span", {"id":"ajaxwinddir"}).text.strip() + "@" + page_soup.find("span", {"id":"ajaxbeaufortnum"}).text.strip()#'Ανεμος: '
    containers5 =  page_soup.find_all("strong")[21].text.strip() + page_soup.find("span", {"id":"ajaxbaro"}).text.strip() +" "+ page_soup.find("span", {"id":"ajaxbarotrendtext"}).text.strip() #+" "+  page_soup.find("span", {"id":"ajaxbarotrendtext"}).text.strip()#'Βαρόμετρο και ταση
    #containers6 = 'max T: ' + page_soup.find("span", {"id":"ajaxtempmax"}).text.strip()
    #containers7 = 'min T: ' +  page_soup.find("span", {"id":"ajaxtempmin"}).text.strip()
    containers6 = 'Βροχή Σήμερα: ' +  page_soup.find("span", {"id":"ajaxrain"}).text.strip()
    containers7 = page_soup.find("td", {"colspan":"2"}).find_all("tr")[1].find_all("td")[0].text.strip() + page_soup.find("table", {"class":"data1"}).find_all('tr')[1].find_all('td')[1].text.strip()
    containers8 =  'Μέγιστη Χθες: ' + page_soup.find("table", {"class":"data1"}).find_all('tr')[1].find_all('td')[2].text.strip()# + page_soup.find("table", {"class":"data1"}).find_all('td')[1].text.strip()
    containers9 =  'Ελάχιστη Σήμερα: ' + page_soup.find("table", {"class":"data1"}).find_all('tr')[2].find_all('td')[1].text.strip() 
    containers10 = 'Ελάχιστη Χθες: ' + page_soup.find("table", {"class":"data1"}).find_all('td')[5].text.strip()
    containers11 =  page_soup.find_all("strong")[20].text.strip() + page_soup.find("span", {"id":"ajaxdew"}).text.strip() #Σημειο δροσου
  # page_soup.find_all("strong")[2].text.strip() 
    containers13 =  page_soup.find_all("strong")[19].text.strip() + page_soup.find("td", {"rowspan":"3"}).find_all('tr')[1].find_all('td')[1].text.strip()# +" "+ page_soup.find("td", {"rowspan":"3"}).find_all('tr')[2].find_all('td')[1].text.strip()
    container14 = page_soup.find_all("strong")[21].text.strip()+"MAX" + page_soup.find("td", {"rowspan":"3"}).find_all('tr')[6].find_all('td')[1].text.strip()
    container15 = "MIN" + page_soup.find("td", {"rowspan":"3"}).find_all('tr')[7].find_all('td')[1].text.strip()
    containers12 = page_soup.find("td", {"colspan":"2"}).find_all("tr")[1].find_all("td")[0].text.strip()#Μεγιστη
    #containers9 = page_soup.find_all("table", {"class":"data1"}.text.strip()
#simeio drosou page_soup.find_all("strong")[20].text.strip()
#broxi simera  page_soup.find("span", {"id":"ajaxtempmax"}).text.strip()
    #containers3 =  page_soup.find_all("strong").text.strip() + page_soup.find_all("span", {"id":"ajaxtempmax"}).text.strip()
    #containers4 =  page_soup
    #
   # norm_containers = unicodedata.normalize('NFKD', containers1).encode('ascii', 'ignore')+ b"\n"
   # the_quote = random.choice(wikiquote.quotes('Richard Feynman')).encode('UTF-8') 
    #output = norm_containers +  the_quote
   # table = [['temp', container14],['feels',container15],['diff', containers1]]
    #return tabulate(table, tablefmt="grid")
    return containers +" / "+ containers3 +"%  / "+ containers4 +" / " + containers5 +" / " + containers0+'% /' + containers1 + " / " + containers2 +" / "+ containers6 +" / "+ containers7 + " / " + containers8 + " / " + containers9  + " / " + containers10  + " / " + containers11   + " / " + containers12  + " / " + containers13  + " / "+ container14 + " / " + container15 # output
#Telepot part    
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, scrap())

TOKEN = '429145952:AAFTuqbZQlnsS6TbmtKvbWwxYbxDp59GkLw'

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(1)
