import csv
import calendar

def head(f):# f== file name
    f="C:\\Users\\bidyut\\csv file\\"+f  # location file create
    hade=['Date','Open','High','Low','Close*','adj_close**','Volume']
    try :
        with open(f,'x',newline='')as op:# give file path 
            f=csv.DictWriter(op,hade)
            f.writeheader()
    except:
        pass
def row(x,f):# x== row value and f== file name
    f="C:\\Users\\bidyut\\csv file\\"+f  # location file create
    try :
        with open(f,'a',newline='')as op:# give file path 
            f=csv.writer(op)
            f.writerow(x)
    except:
        pass

def month(x):
    Month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    date=x.replace("-"," ")
    wk=(date[3:6])
    m=int(Month.index(wk))+1
    y=int(date[7:11])
    d=int(date[0:2])
    return y,m,d

def week(d): # return week day
    x=month(d)
    y=x[0] # year
    m=x[1] # month
    d=x[2] # date
    week_day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    d_num=calendar.weekday(y,m,d)
    day_name=week_day[d_num]
    return day_name


def duplicate(l): #chake duplicate in list
    if len(l)==len(set(l)):
        return False
    else:
        return True


def list_clear(x):# list clear if (list_lenth ==5)
    y=list(x)
    if len(y)>=5:
        y.clear()
    return y


def dayinlist_limit(a,g):# get days in two list uncomon days
    b=['Friday','Monday','Tuesday','Wednesday','Thursday']
    l=[]
    l.clear()
    for x in b:
        if x not in a:
            l.append(x)
            if x == g:
                break
    return l

def text(x,file):
    fn=file+".txt"
    f="C:\\Users\\bidyut\\csv file\\"+fn  # location file create
    t=x+"\n"
    try:
        with open(f,'x')as op:
            op.write(t)
    except:
        with open(f,'a')as op:
            op.write(t)


def dervace_box_csv(f): # main_program
    week_list=[]
    count_list=[]
    count=0
    f=f.split("\\")
    f=f[-1]
    with open(f,'r')as op:
        file=csv.reader(op)
        next(file)
        for x in reversed(list(file)):
            date=x[0]
            week_day=week(date)
            week_list=list_clear(week_list)
            #***************creat_new_file*******************************#
            if week_day=="Friday"and (len(week_list)==4 or 3 or 2 or 1 or 0)and(duplicate(week_list)==False):
                week_list.clear()
                week_list.extend(dayinlist_limit(week_list,week_day))
                count_list.clear()
                count_list.append(count)
                file_name=str(count_list[-1])+"__"+f
                head(file_name)
                row(x,file_name)
                fn=f.strip(".csv")
                text(file_name,fn)
                

            #***********************creat_new_file***********************#
            elif week_day=="Monday"and (len(week_list)==0)and(duplicate(week_list)==False):
                week_list.clear()
                week_list.extend(dayinlist_limit(week_list,week_day))
                count_list.clear()
                count_list.append(count)
                file_name=str(count_list[-1])+"__"+f
                head(file_name)
                row(x,file_name)
                fn=f.strip(".csv")
                text(file_name,fn)


            #******************creat_new_file****************************#
            elif week_day=="Tuesday"and (len(week_list)==0)and(duplicate(week_list)==False):
                week_list.clear()
                week_list.extend(dayinlist_limit(week_list,week_day))
                count_list.clear()
                count_list.append(count)
                file_name=str(count_list[-1])+"__"+f
                head(file_name)
                row(x,file_name)
                fn=f.strip(".csv")
                text(file_name,fn)
                

            #****************creat_new_file******************************#
            elif week_day=="Wednesday"and (len(week_list)==0)and(duplicate(week_list)==False):
                week_list.clear()
                week_list.extend(dayinlist_limit(week_list,week_day))
                count_list.clear()
                count_list.append(count)
                file_name=str(count_list[-1])+"__"+f
                head(file_name)
                row(x,file_name)
                fn=f.strip(".csv")
                text(file_name,fn)

            #******************creat_new_file****************************#
            elif week_day=="Thursday"and (len(week_list)==0)and(duplicate(week_list)==False):
                week_list.clear()
                week_list.extend(dayinlist_limit(week_list,week_day))
                count_list.clear()
                count_list.append(count)
                file_name=str(count_list[-1])+"__"+f
                head(file_name)
                row(x,file_name)
                fn=f.strip(".csv")
                text(file_name,fn)


#__________________________________________________________________________________________________

            elif week_day=="Monday"and (len(week_list)==1)and(duplicate(week_list)==False):
                week_list.extend(dayinlist_limit(week_list,week_day))
                file_name=str(count_list[-1])+"__"+f
                row(x,file_name)
                

            elif week_day=="Tuesday"and (len(week_list)==2 or 1)and(duplicate(week_list)==False):
                week_list.extend(dayinlist_limit(week_list,week_day))
                file_name=str(count_list[-1])+"__"+f
                row(x,file_name)
                

            elif week_day=="Wednesday"and (len(week_list)==3 or 2 or 1)and(duplicate(week_list)==False):
                week_list.extend(dayinlist_limit(week_list,week_day))
                file_name=str(count_list[-1])+"__"+f
                row(x,file_name)
                

            elif week_day=="Thursday"and (len(week_list)==4 or 3 or 2 or 1)and(duplicate(week_list)==False):
                week_list.extend(dayinlist_limit(week_list,week_day))
                file_name=str(count_list[-1])+"__"+f
                row(x,file_name)
                


            else:
                print(count,"else:___",week_day,date)
                break
            count+=1


dervace_box_csv("SBIN.csv")