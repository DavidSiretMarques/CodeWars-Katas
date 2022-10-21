"""
Solution to the CodeWars kata More Zeros than Ones
Link:
https://www.codewars.com/kata/5d41e16d8bad42002208fe1a
"""

def more_zeros(s):
    #Create a moreZeros function which will receive a string for input, and return an array (or null terminated string in C) containing only the characters from that string whose binary representation of its ASCII value consists of more zeros than ones.
    # You should remove any duplicate characters, keeping the first occurence of any such duplicates, so they are in the same order in the final array as they first appeared in the input string.
    res=[]
    for i in range(len(s)):
        bincode=bin(ord(s[i]))[2:]
        if bincode.count('0')>bincode.count('1'):
            if s[i] not in res:
                res.append(s[i])        
    return res

# --------------------------------------------Extras--------------------------------------------

#Other solutions

def more_zeros2(s):
    results = []
    for letter in s:
        dec_repr = bin(ord(letter))[2:]
        if (dec_repr.count("0") > dec_repr.count("1")) and (letter not in results):
            results.append(letter)
    return results
