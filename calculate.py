import argparse
import math_lib

def parse_args():
    parser = argparse.ArgumentParser(
        description = 'This program calculate add/div of given inputs' 
    )
    parser.add_argument('inputs',
                        type=float,
                        nargs='+',
                        help='two input numbers'
    )

    args_parse = parser.parse_args()

    return args_parse

if __name__ == '__main__':
    args = parse_args()
    if (len(args.inputs) < 2):
        print('must input 2 numbers')
    else:
        a = args.inputs[0]
        b = args.inputs[1]
        print('your input values are: %f and %f' % (a, b))
        print('the sum is %f' % math_lib.add(a, b))
        print('first/second is %f' % math_lib.div(a, b))
