#!/usr/bin/python3
def print_last_digit(number):
    """Print and return the last digit of a number."""
    last_digit = number % 10 if number >= 0 else -(-number % 10)
    print("{:d}".format(abs(last_digit)), end="")
    return abs(last_digit)
