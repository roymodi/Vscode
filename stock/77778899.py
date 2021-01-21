from requests_html import HTMLSession


def weblist():
    session=HTMLSession()
    url=session.get('https://www.moneycontrol.com/india/stockpricequote/')
    co=url.html.find('.pcq_tbl',first=True).text
    co_list=(co.replace("\n",",")).split(",") # this is ok list
    return co_list

def stringlenth(x,y):
    lis=(x.lower()).replace(" ","") #list string
    ins=(y.lower()).replace(" ","") # input string
    l=[]
    count=1
    for x in ins:
        if len(ins)>len(lis):
            continue
        elif x==lis[count-1]:
            l.append(count)
        else:
            continue
        count+=1
    return (len(l))


def repetlist(x):
    maxx=max(x)
    maxxlis=[]
    count=0
    for y in x:
        if y==maxx:
            maxxlis.append(count)
        count+=1
    return maxxlis


def str_len_list(l,i):
    lentlis=[]
    for x in l:
        lent=stringlenth(x,i)
        lentlis.append(lent)
    return lentlis


def linklist(l,i):
    i=i.upper()
    for x in l:
        y=x.split("/")
        if (len(y))==8 and (y[-1].replace("'",''))==i:
            nli=(x.replace("href=",'')).replace("'",'')
            return nli
        elif (len(y))==8 and ((y[-2]).upper())==i:
            nli=(x.replace("href=",'')).replace("'",'')
            return nli
   


def quote(link):
    session=HTMLSession()
    url=session.get(link)
    bse=url.html.find('.bsedata_bx > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)',first=True).text
    nse=url.html.find('.nsedata_bx > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)',first=True).text
    return ('NSE: '+nse,'BSE: '+bse)

def get_quote(x):
    s=x
    li=weblist()

    lenlist=str_len_list(li,s)
    replis=repetlist(lenlist)

    session=HTMLSession()
    url=session.get('https://www.moneycontrol.com/india/stockpricequote/')

    for x in replis:
        if (((li[x]).replace(" ","")).upper())==(s.upper()):
            coo=str(li[x])
            link=url.html.find('a',containing=coo)
            p=linklist((str(link)).split(),coo)
            try:
                stock=quote(p)
                return stock
            except:
                colink=((str((str(link).split(" "))[2]).split("="))[1]).replace("'",'')
                stock=quote(colink)
                return stock
            break
        else:
            return ("Your Suggestion is: "+(li[x]))





#print(get_quote(input("stock: ")))