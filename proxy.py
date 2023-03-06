import requests,urllib,threading,os
from threading import active_count
os.system('pip install requests')
os.system('pip install urllib') 
os.system('pip install threading') 
n_threads = 100  
threads = []
def scrap():
    try:
        https = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=0", proxies=urllib.request.getproxies(), timeout=5).text
        http = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=0", proxies=urllib.request.getproxies(), timeout=5).text
        socks = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=0", proxies=urllib.request.getproxies(), timeout=5).text
    except Exception as e:
        print(e)
        return False
    f = open("proxies.txt", "w")
    f.write(https+"\n"+http)
    f.close()
    f = open("socks.txt", "w")
    f.write(socks)
    f.close()
def checker(proxy):
    proxies = {
        'http': proxy,
        'https': proxy,}
    try:
        view2(proxy)
    except Exception as e:
        return False
def start():
    s = scrap()
    if s == False:
        return
    list = open('proxies.txt', 'r')
    proxies = list.readlines()
    list.close()
    for i in proxies:
        p = i.split('\n')[0]
        if not p:
            continue
        while active_count() > n_threads:
            liiii=9
        thread = threading.Thread(target=checker, args=(p,))
        threads.append(thread)
        thread.start()
    list = open('socks.txt', 'r')
    proxies = list.readlines()
    list.close()
    for i in proxies:
        p = i.split('\n')[0]
        if not p:
            continue
        while active_count() > n_threads:
          lii7ii=99
        pr = "socks5://"+p
        thread = threading.Thread(target=checker, args=(pr,))
        threads.append(thread)
        thread.start()
    return True
def process(run_for_ever:bool = False):
    if run_for_ever:
        while True:
            start()
    else:
        start()
process(True)
