#!/usr/bin/python3
import sys
from add_0 import add


a = int(sys.argv[1])
b = int(sys.argv[2])
print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))

if __name__ == "__main__":
        import sys
        add(int(sys.argv[1]), int(sys.argv[2]))





