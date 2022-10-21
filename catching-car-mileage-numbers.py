"""
Solution to the CodeWars kata Catching Car Mileage Numbers
Link:
https://www.codewars.com/kata/52c4dd683bfd3b434c000292/python
"""


def is_interesting(number, awesome_phrases):
    #Write the function that parses the mileage number input, and returns a 2 if the number is "interesting" (see below), a 1 if an interesting number occurs within the next two miles, or a 0 if the number is not interesting.
    #loop over all the posible awesome numbers related to the one given
    for num in [number, number+2,number+1]:
        #checking it's over 99
        if len(str(num))<3:
            continue
        #checking it's in awesome_phrases
        if num in awesome_phrases:
            if num==number:
                return 2
            return 1
        #checking it's number followed by all 0's
        if str(num).count("0")==len(str(num))-1:
            if num==number:
                return 2
            return 1
        #Checking it's same number repeated
        eqval=[]
        for ch in str(num):
            eqval.append(ch==str(num)[0])
        if all(eqval):
            if num==number:
                return 2
            return 1
        #Checking increasing or decreasing number
        if "1234567890".find(str(num))!=-1 or "9876543210".find(str(num))!=-1:
            if num==number:
                return 2
            return 1
        #Checking for pallindromic numbers
        palindrome=[]
        for i in range(len(str(num))//2):
            palindrome.append(str(num)[i]==str(num)[-i-1])
        if all(palindrome):
            if num==number:
                 return 2
            return 1
    return 0   

# --------------------------------------------------Extras--------------------------------------------------

def is_interesting(number, awesome_phrases):
    #Another solution to the kata
    for r, num in zip((2, 1, 1), range(number, number + 3)):
        num_str = str(num)
        if num in awesome_phrases or num > 99 and (int(num_str[1:]) == 0 or num_str[::-1] == num_str or num_str in '1234567890' or num_str in '9876543210'):
            return r
    return 0