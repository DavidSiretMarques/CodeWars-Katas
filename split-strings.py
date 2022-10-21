"""
Solution to the CodeWars kata Split Strings
Link:
https://www.codewars.com/kata/515de9ae9dcfc28eb6000001
"""

def splitString(s):
    #Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
    res=[]
    for i in range(0,len(s),2):
        if i<len(s)-1:
            res.append(s[i]+s[i+1])
        else:
            res.append(s[i]+"_")
    return res  

def splitString2(s):
    #Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result
