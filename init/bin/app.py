
import argparse

from init.lib.operation import Math


def main():
    
    parser = argparse.ArgumentParser(description='Arguments for Algebric Operation')
    parser.add_argument('operation', metavar='OPERATION', help='Operation to perform')
    parser.add_argument('a', metavar='N', help='Number 1')
    parser.add_argument('b', metavar='N', help='Number 2')
    args = parser.parse_args()
    a = float(args.a)
    b = float(args.b)
    
    math = Math()
    
    if args.operation in ['add', 'sum']:
        result = math.add(a, b)
    elif args.operation in ['substract', 'minus']:
        result = math.substract(a, b)
    elif args.operation in ['multiply', 'times']:
        result = math.multiply(a, b)
    elif args.operation in ['divide']:
        result = math.divide(a, b)
    else:
        raise TypeError('Unknown Operaton [sum, sustract, multiply, divide]')
    
    print(f'{a} ({args.operation}) {b} :=> {result}')
    exit(0)

if __name__ == "__main__":
    main()
