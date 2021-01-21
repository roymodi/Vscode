import json
import os

import pickle
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

"url = https://httpbin.org/ip"
class Webscraping:
    def __init__(self):
        self.proxy_url = "https://sslproxies.org/"

    def create_path(self):
        folder_name = 'Temp_file'  # this is folder name
        current_dir = os.getcwd()  # this is path
        path = os.path.join(current_dir, folder_name)  # create folder path
        try:
            os.mkdir(path)
        except FileExistsError:
            pass
        return path
    
    def creatname(self,url):
        nstr = (url.replace('https://','')).split('.')
        try:
            str1 = nstr[1]
            # remove any spacial charater 
            sr = (''.join(x for x in str1 if x.isalpha()))
        except IndexError:
            str1 = nstr[0]
            sr = (''.join(x for x in str1 if x.isalpha()))
        except :
            str1 = "Defult"
            sr = (''.join(x for x in str1 if x.isalpha()))
        return sr

    def proxy_generator(self,url):
        response = requests.get(self.proxy_url)
        soup = BeautifulSoup(response.content, 'html5lib')
        proxy = ((list(map(lambda x: x[0] + ':' + x[1], list(
            zip(map(lambda x: x.text, soup.findAll('td')[::8]), map(lambda x: x.text, soup.findAll('td')[1::8]))))))[0:100])
        
        jurl = self.creatname(url) + '.json'  # this is for create new name every time url change
        pg_file = self.create_path() + '\\' + jurl
        with open(pg_file, 'w')as op:
            json.dump(proxy, op)

    def jproxy(self,url):
        flist = os.listdir(self.create_path())
        jurl = self.creatname(url) + '.json'  # this is for create new name every time url change
        jp_file = self.create_path() + '\\' + jurl
        if jurl in flist:
            with open(jp_file, 'r')as op:
                jlod = json.load(op)
        else:
            self.proxy_generator(url)
            with open(jp_file, 'r')as op:
                jlod = json.load(op)
        return jlod

    def cokiere(self,url):
        flist = os.listdir(self.create_path()) # list of file in path
        nurl = self.creatname(url)  # pickle file name
        # time url change
        ck_nurl = self.create_path() + '\\' + nurl # pickle file path
        if nurl in flist:
            with open(ck_nurl, 'rb')as op:
                newcokie = pickle.load(op)
            if len(newcokie) == 0:
                jscokie = None
            else:
                jscokie = newcokie
        else:
            jscokie = None
        return jscokie
    def web(self,*args):
        dic = args[-1]
        auth = dic['auth'] if 'auth' in dic.keys() else None
        params = dic['params'] if 'params' in dic.keys() else None
        cert = dic['cert'] if 'cert' in dic.keys() else None
        stream = dic['stream'] if 'stream' in dic.keys() else False
        data = dic['data'] if 'data' in dic.keys() else None
        json = dic['json'] if 'json' in dic.keys() else None
        files = dic['files'] if 'files' in dic.keys() else None
        method =(dic['method']).upper() if 'method' in dic.keys() else 'GET'
        url = args[0]
        proxy = args[1]
        _ua = args[2]
        jcoke = args[3]
        if method == 'POST':
            res = requests.post(url,timeout=7, proxies=proxy, headers=_ua, cookies=jcoke, auth=auth, params=params, cert=cert, stream=stream, data=data, json=json, files=files)
            pass
        else:
            res = requests.get(url, timeout=7, proxies=proxy, headers=_ua, cookies=jcoke, auth=auth, params=params, cert=cert, stream=stream)
        return res

    def webpage(self,url,**kwargs):
        ua = UserAgent()
        jcoke = self.cokiere(url)
        # this is for create new name if every time url change (string value return)
        gjurl = self.creatname(url) + 'goodproxy.json' 
        # this is temp_file in goodproxy.json file link
        wp_gjurl = self.create_path() + '\\' + gjurl
        # this is goodproxy.json file
        file = os.listdir(self.create_path())
        count = 0
        while True:
            hd = ua.random  # random user agent only
            _ua = {'User-Agent': hd}
            try:
                try:
                    with open(wp_gjurl, 'r')as op:
                        old_proxy = json.load(op)
                    res = self.web(url, old_proxy, _ua, jcoke, kwargs)
                    return res
                    break

                except FileNotFoundError:
                    pxy = (self.jproxy(url))[count]
                    proxy = dict(https=pxy)
                    res = self.web(url, proxy, _ua, jcoke, kwargs)
                    with open(wp_gjurl, 'w')as op:
                        json.dump(proxy, op)
                    nurl = self.creatname(url)
                    ck_nurl = self.create_path() + '\\' + nurl
                    with open(ck_nurl, 'wb')as f:
                        pickle.dump(res.cookies, f)
                    if count ==100:
                        count -=100
                        self.proxy_generator(url)
                    else:
                        pass
                    return res
                    break

                except :
                    os.remove(wp_gjurl)
                    pxy = (self.jproxy(url))[count]
                    proxy = dict(https=pxy)
                    res = self.web(url, proxy, _ua, jcoke, kwargs)
                    with open(wp_gjurl, 'w')as op:
                        json.dump(proxy, op)
                    nurl = self.creatname(url)
                    ck_nurl = self.create_path() + '\\' + nurl
                    with open(ck_nurl, 'wb')as f:
                        pickle.dump(res.cookies, f)
                    if count ==100:
                        count -=100
                        self.proxy_generator(url)
                    else:
                        pass
                    return res
                    break

            except:
                pass
            count +=1