"""
Solution to the CodeWars kata Sum of Digits/Digital Root
Link:
https://www.codewars.com/kata/541c8630095125aba6000c00
"""

def digital_root(n):
    #A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.
    while len(str(n))>1:
        sum=0
        for ch in str(n):
            sum+=int(ch)
        n=sum
    return n

# --------------------------------------------Extras--------------------------------------------

#Other solutions

def digital_root2(n):
    #A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.
    while n>10:
        n = sum([int(i) for i in str(n)])
    return n