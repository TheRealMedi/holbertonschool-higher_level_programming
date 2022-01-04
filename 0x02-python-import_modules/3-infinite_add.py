#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
    for arg in sys.argv[1:]:
        add += int(arg)
    print("{:d}".format(add))
