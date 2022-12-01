#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    from sys import argv, exit
    if (len(argv) - 1) != 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if argv[2] == '+':
        print("{} + {} = {}".format(a, b, calc.add(a, b)))
    elif argv[2] == '-':
        print("{} - {} = {}".format(a, b, calc.sub(a, b)))
    elif argv[2] == '*':
        print("{} * {} = {}".format(a, b, calc.mul(a, b)))
    elif argv[2] == '/':
        print("{} / {} = {}".format(a, b, calc.div(a, b)))
    else:
        print("Unknown operator. Available operators:", end='')
        print(" +, -, * and /")
        exit(1)
