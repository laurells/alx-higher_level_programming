#!/usr/bin/python3
def uppercase(str):
    tmp = ""
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            tmp += chr(ord(c)-32)
        else:
            tmp += c
    print("{}".format(tmp))
