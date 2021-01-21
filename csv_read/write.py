import csv

# write csv file normal
a=input()
with open("python_file\\csv_read\\file\\read_2.csv",'a',newline='')as f:
    writer=csv.writer(f)
    writer.writerow(a)

# read csv file normal 
with open ('python_file\\csv_read\\file\\read_2.csv','r',newline='')as f:
    reader=csv.reader(f,delimiter=':',quoting=csv.QUOTE_NONE)
    for x in reader:
        print(x)
