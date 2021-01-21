file=open('file_handaling\\sample.txt','r')
#line = file.readlines() 

# file handle file
while True:
    # read line
    line = file.readline()
    # in python 3
    a=line
    print(a)
    # check if line is not empty
    if not line:
        break
file.close()