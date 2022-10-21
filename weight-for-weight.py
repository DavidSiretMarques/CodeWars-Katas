"""
Solution to the CodeWars kata Weight for weight
Link:
https://www.codewars.com/kata/55c6126177c9441a570000cc/python

"""

def order_weight(strng):
    #Function that orders a string of numbers separated by space by the sum of its digits. If two numbers sum the same, consider them strings, the shortest one goes first.
    result=[]
    answer=[]
    numbers=sorted(strng.split())
    for item in numbers:
        weight=0
        for ch in item:
            weight+=int(ch)
        result.append([weight,item])
    result.sort()
    for item in result:
        answer.append(str(item[1]))
    return " ".join(answer)

# --------------------------------------------Extras--------------------------------------------

#Other solutions
def order_weight2(strng):
    #Function that orders a string of numbers separated by space by the sum of its digits. If two numbers sum the same, consider them strings, the shortest one goes first.
    initial_list = sorted(strng.split())
    result = " ".join(sorted(initial_list, key=sum_string))
    return result

def sum_string(s):
    #Function used in order_weight2
    sum = 0
    for digit in s:
        sum += int(digit)
    return sum


