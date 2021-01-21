import csv

file_name='SBIN.csv'

BC_file = open(file_name, 'r')
BC_reader = csv.reader(BC_file)
next(BC_reader) # this is for pass header in csv file.
for row in reversed(list(BC_reader)):
    print (row)