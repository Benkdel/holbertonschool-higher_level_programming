#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    name_exec = sys.argv[0]
    for item in sys.argv:
        if name_exec != item:
            result += int(item)
    print(result)
