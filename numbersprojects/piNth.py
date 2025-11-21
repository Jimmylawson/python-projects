#generate a pi to the nth digit
import math
from decimal import Decimal, getcontext


def NthDigit():
    """
    Calculate π to the nth decimal place.
    Handles invalid inputs and negative numbers gracefully.
    """
    try:
        n = int(input("Enter a number for the decimal places of pi: "))
        if n < 0:
            print("Please enter a positive number")
            return
        if n > 1000: # Prevent excessive computations
            print("Please enter a number less than 1000")
            return
        getcontext().prec = n + 1
        pi = Decimal(math.pi)
        print(f"n to {n} decimal places: {pi:.{n}f}")
    except ValueError:
        print("Please enter a valid number")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return



NthDigit()