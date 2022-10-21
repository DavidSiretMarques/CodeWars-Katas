"""
Solution to the CodeWars kata Highest and lowest
Link:
https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
"""


def high_and_low(numbers):
    #Use map to convert the strings of the splitted original to int, then max/min to locate
        return str(max(list(map(int,numbers.split(' ')))))+' '+str(min(list(map(int,numbers.split(' ')))))

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))

# --------------------------------------------Extras--------------------------------------------

#Other solutions

def high_and_low(numbers):
    #In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
    #Output string must be two numbers separated by a single space, and highest number is first.
    numberlist=numbers.split()
    for i in range(0,len(numberlist)):
        numberlist[i]=int(numberlist[i])
    return str(max(numberlist))+" "+str(min(numberlist))

def high_and_low2(numbers):
    #In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
    #Output string must be two numbers separated by a single space, and highest number is first.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
