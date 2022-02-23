"""01-Task1-Task2
Write a Python-script that performs the standard math functions on the data. The name of function and data are
set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py add 1 2

Notes:
Function names must match the standard mathematical, logical and comparison functions from the built-in libraries.
The script must raises all happened exceptions.
For non-mathematical function need to raise NotImplementedError.
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""

import argparse
import operator
import math

parser = argparse.ArgumentParser()
parser.add_argument("operator", type=str, help="Operator")
parser.add_argument("number_a", type=float, help="First argument")
parser.add_argument("number_b", type=float, help="Second argument")


def calculate(args):
    """
    Function tries to find a mathematical function of given name in modules
    'operator'. If it succeeds, it calculates it\'s value with given arguments.

    :param args: a container for number_a (float), operator (string), number_b (float)
    :return: float, result of execution of chosen function with given arguments
    """

    func = hasattr(operator, args.operator) and getattr(operator, args.operator) or \
           hasattr(math, args.operator) and getattr(math, args.operator)
    if func:
        return func(args.number_a, args.number_b)
    raise NotImplementedError


def main():
    args = parser.parse_args()
    print('The operation completed. Result:', calculate(args))


if __name__ == '__main__':
    main()
