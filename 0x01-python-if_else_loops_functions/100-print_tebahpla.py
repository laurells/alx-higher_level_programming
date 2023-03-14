#!/usr/bin/python3
tmp = ""
for i in reversed(range(97, 123)):
    if (i % 2) == 0:
        tmp += chr(i)
    else:
        tmp += chr(i-32)
print("{}".format(tmp), end="")
