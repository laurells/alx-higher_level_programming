#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    i = 0
    for a in sys.argv:
        if i > 0:
            sum += int(a)
        i += 1
        print(sum)
