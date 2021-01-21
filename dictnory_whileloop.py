import csv
data={'hi':'hello'}
file=open('chat_bot\\data\\data.csv','a')
data_write=csv.DictWriter(file,data.keys())
data_write.writerow(data)
data_write_value=csv.DictWriter(file,data.values())
data_write_value.writerows(data)


while True:
    key=input("you: ")
    if key in data:
        value=data.get(key)
        print(value)
    elif key not in data:
        data[key]=None
        tech=input("teach: ")
        data[key]=tech

    

