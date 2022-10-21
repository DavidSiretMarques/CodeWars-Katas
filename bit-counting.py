"""
Solution to the kata Bit Counting
Link:
https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python
"""



def count_bits(n):
    #Use the binary built-in function and remove the start (binary numbers start with 0b to sifnigy they're binary)
    return bin(n)[2:].count('1')

# --------------------------------------------Extras--------------------------------------------

#Other solutions

def countBits(n):
    #Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.
    # Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
    number=bin(int(n))
    #bin gives back the binary code in the form "0bbinarycode", so we have to quit the two first
    number=number[2:]
    sum=0
    for ch in number:
        sum+=int(ch)
    return sum


def countBits2(n):
    #Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.
    # Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
    return bin(n).count("1")

