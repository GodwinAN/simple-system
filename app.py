# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

def oddoreven(num):
    if (num % 2) == 0:
        return("{0} is Even".format(num))
    else:
        return("{0} is Odd".format(num))
        pass
oddoreven(int(input()))
