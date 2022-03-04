import requests
from bs4 import BeautifulSoup
import time

#  BotFather:  t.me/sin0nimbot  ID = 1958512029
BOT_KEY = '5203210837:AAEzPE_JgMnJHQhxsTahLSP3xP75jepQZS0'
TG_API = 'https://api.telegram.org/bot'
CHAT_ID = "1958512029"
#print(TG_API + BOT_KEY + "/getUpdates")

message_url = TG_API + BOT_KEY + f"/sendMessage?chat_id={CHAT_ID}&text=forabank.ru сurrent exchange rate "
requests.get(message_url)

while True:
    bank_url = 'https://www.forabank.ru/exchange/'

    bank_data = requests.get(bank_url)
    #print(bank_data.status_code)
    bank_soup = BeautifulSoup(bank_data.content, "html.parser")
    elements = bank_soup.findAll(class_="content-right-courses-item-value")
    usd = elements[0].string.strip()
    kurs = f'1 USD = {usd} RUB'
    print(kurs)
    message_url = TG_API + BOT_KEY + f"/sendMessage?chat_id={CHAT_ID}&text={kurs}"
    requests.get(message_url)
    time.sleep(1800)
