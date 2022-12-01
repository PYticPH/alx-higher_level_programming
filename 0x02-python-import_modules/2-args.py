#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if (len(argv) < 2):
        print("{} arguments.".format(len(argv) - 1))
    else:
        print("{} arguments".format(len(argv) - 1))
        for num in range(1, len(argv)):
            print("{}: {}".format(num, argv[num]))
