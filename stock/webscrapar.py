from random import choice
import requests,pickle
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json
import os 
import datetime


def proxy_generator():
    response = requests.get("https://sslproxies.org/")
    soup = BeautifulSoup(response.content, 'html5lib')
    proxy=((list(map(lambda x:x[0]+':'+x[1], list(zip(map(lambda x:x.text, soup.findAll('td')[::8]), map(lambda x:x.text, soup.findAll('td')[1::8]))))))[0:100])
    with open('proxy.json','w')as op:
        json.dump(proxy,op)
        
#print(proxy_generator())


def jproxy():
    flist=os.listdir(os.getcwd())
    if 'proxy.json'in flist:
        with open('proxy.json','r')as op:
            jlod=json.load(op)
    else:
        proxy_generator()
        path=os.getcwd()
        with open((path+'\\proxy.json'),'r')as op:
            jlod=json.load(op)
    return jlod

def cokieRe(url):
    flist=os.listdir(os.getcwd())
    nurl=''.join(x for x in url if x.isalpha())# remove all spacial charater and number
    if nurl in flist:
        with open(nurl,'rb')as op:
            jscokie=pickle.load(op)
    else:
        jscokie=None
    return jscokie


def webpage(url):
    ua=UserAgent()
    jcoke=cokieRe(url)
    count=0
    while True:
        file=os.listdir(os.getcwd())
        hd=ua.random #random user agent only
        UA={'User-Agent':hd}
        if 'goodpoxy.json' in file:
            try:
                path=os.getcwd()
                with open((path+'\\goodpoxy.json'),'r')as op:
                    old_proxy=json.load(op)
                res=requests.get(url,proxies=old_proxy,timeout=7,headers=UA,cookies=jcoke)
                break
            except:
                os.remove((path+'\\goodpoxy.json'))
                pass

        elif count==100:
            count-=100
            proxy_generator()

        else:
            try:
                pxy=(jproxy())[count]
                proxy=dict(https=pxy)
                res=requests.get(url,proxies=proxy,timeout=7,headers=UA,cookies=jcoke)
                with open('goodpoxy.json','w')as op:
                    json.dump(proxy,op)
                print(proxy)
                break
            except:
                pass

        count+=1
    nurl=''.join(x for x in url if x.isalpha()) # remove all spacial charater and number
    # this creat pickel file for cookies in bynary from
    with open(nurl,'wb')as f:
        pickle.dump(res.cookies,f)
    return res

print(webpage("https://www.google.com"))