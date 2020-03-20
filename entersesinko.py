from fake_useragent import UserAgent
import requests
import time
import datetime
from time import sleep
from faker import Faker
import random
from proxymanager import ProxyManager

proxy_manager = ProxyManager('proxies.txt')


fake = Faker()
with open('emails.txt') as f:
    content = f.read().splitlines()
print(content)

with open('instagram.txt') as p:
    insta = p.read().splitlines()
ua = UserAgent()

headers = {
    "Host": "formbuilder.hulkapps.com",
    "User-Agent": ua.random,
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://formbuilder.hulkapps.com/corepage/customform?id=UrdDlFI0Cj-uOz8ePbBQrQ",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest"
    }
link = "https://formbuilder.hulkapps.com/ajaxcall/formresponse"



for i in content: 
   
    firstname = fake.first_name()
    secondname = fake.last_name()
    instagram = random.choice(insta)
    random_proxy = proxy_manager.random_proxy() 
    i
    payload = {
    "form_uuid":"UrdDlFI0Cj-uOz8ePbBQrQ",
    "formResponse":"{\"First+Name\":" + firstname + ",\"Last+Name\":" + secondname + ",\"Email+Address+(PayPal)\":" +  i + ",\"Instagram\":" + instagram + ",\"Size+(US)\":\"11\"}",
    "confirmationMail":i,
    "is_pro":"false"
    }
    proxy = {
        "https":random_proxy.get_dict()["https"]
    }
    entry = requests.post(link, headers=headers, data=payload, proxies=proxy)
    print(entry.text)
    sleep(2)
    
