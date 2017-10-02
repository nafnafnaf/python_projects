import sys, time, telepot, unicodedata, urllib3, wikiquote, random
from telepot.loop import MessageLoop
from urllib.request import urlopen, Request #as uReq
from bs4 import BeautifulSoup as soup
#BeautifulSoup + Wikiquote part
def scrap():
    url = 'http://URL/'
    req = urlopen(url)
    page = req.read()
    req.close()
    page_soup = soup(page, "html.parser")
    #-1-containers = page_soup.find("span", {"id":"ajaxtemp"}).find("span",{"class":"ajax"})
    #-2-containers = page_soup.find("span", {"id":"ajaxfeelslike"}).text.strip()
    containers = "Διαφορα ωρας" +page_soup.find_all("strong")[1].text.strip()
#    norm_containers = unicodedata.normalize('NFKD', containers).encode('ascii', 'ignore')+ b"\n"
   # the_quote = random.choice(wikiquote.quotes('Richard Feynman')).encode('UTF-8') 
    #output = norm_containers +  the_quote
    return containers# output
#Telepot part    
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, scrap())

TOKEN = 'TOKEN'

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(1)
