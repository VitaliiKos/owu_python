"""01-Task1-Task1
Write a Python-script that performs simple arithmetic operations: '+', '-', '*', '/'. The type of operator and
data are set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py 1 * 2

Notes:
For other operations need to raise NotImplementedError.
Do not dynamically execute your code (for example, using exec()).
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""

import argparse
from operator import add, mul, truediv, sub

parser = argparse.ArgumentParser()
parser.add_argument("number_a", type=float, help="First argument")
parser.add_argument("operator", type=str, help="Operator")
parser.add_argument("number_b", type=float, help="Second argument")

operators = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv

}


def calculate(args):
    """
    :param args: a container for number_a (float), operator (string), number_b (float)
    :return: float, result of operation
    """

    if args.operator in operators.keys():
        return operators[args.operator](args.number_a, args.number_b)
    raise NotImplementedError


def main():
    args = parser.parse_args()
    print('The operation completed. Result:', calculate(args))


if __name__ == '__main__':
    main()
