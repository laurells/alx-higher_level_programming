#!/usr/bin/python3
def remove_char_at(str, n):
    tmp = ""
    cont = 0
    for c in str:
        if cont == n:
            pass
        else:
            tmp += c
        cont += 1
    return tmp
