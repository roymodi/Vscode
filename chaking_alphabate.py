def char(x):# chaking alphabate
    string=x
    only_char=""
    for char in string:
        if char.isalpha():
            only_char +=char
    return only_char

if __name__ == "__main__":
    print(char('jadfjashsdkjd215dfsdasv446fg4654g6ds4fgdf'))