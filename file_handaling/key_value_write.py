file=open('file_handaling\\new_2.txt','a')

def key():
    text=input('key: ')
    lr=text.casefold()
    file.write(lr)


    value()

def value():
    text=input('val: ')
    lr=text.casefold()
    val=':'+lr+'\n'
    file.write(val)

    file.close()



key()

