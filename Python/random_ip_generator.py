"""
Author: Akshay Joshi
GitHub: https://github.com/ijoshi90
Creation Date: 22.10.24

Description: Random Generator
"""

from random import *

def generateIPv4Segment():
    return randrange(0,255)

def generateIPv6Segment():
    """
    Generate one segment of an IPv6 address.

    Returns:
    str: A 4-character hexadecimal string representing one segment of an IPv6 address.
    """
    # Generate a random 16-bit number
    segment = randint(0, 0xffff)
    # Format it as a 4-character hexadecimal string
    return f"{segment:04x}"

# Main function
if __name__ == '__main__':
    randomNumbersIPv4 = [str(generateIPv4Segment()), generateIPv4Segment().__str__(), str(generateIPv4Segment())]
    randomIPv4 = '.'.join(randomNumbersIPv4)

    randomNumbersIPv6 = [
                            str(generateIPv6Segment()), generateIPv6Segment().__str__(), str(generateIPv6Segment()),\
                            str(generateIPv6Segment()), generateIPv6Segment().__str__(), str(generateIPv6Segment())
                         ]
    randomIPv6 = ':'.join(randomNumbersIPv6)

    print("Generated Random IPv4 : {}".format(randomIPv4))
    print("Generated Random IPv6 : {}".format(randomIPv6))
