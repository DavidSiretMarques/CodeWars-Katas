"""
Solution to the CodeWars kata Does my number look big in this?
Link:
https://www.codewars.com/kata/5287e858c6b5a9678200083c
"""

def narcissistic( value ):
    #A Narcissistic Number is a number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).
    # For example, take 153 (3 digits): 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 and 1634 (4 digits): 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634 
    # The Challenge: Your code must return true or false depending upon whether the given number is a Narcissistic number in base 10.
    number=str(value)
    num=0
    for ch in number:
        num+=int(ch)**len(number)
    return num==value

# --------------------------------------------Extras--------------------------------------------

#Other solutions

def narcissistic2( value ):
    vstr = str(value)
    nvalue = sum(int(i)**len(vstr) for i in vstr)
    return nvalue == value
