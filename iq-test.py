"""
Solution to the CodeWars kata IQ Test
Link:
https://www.codewars.com/kata/552c028c030765286c00007d
"""

def iq_test(numbers):
    #Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.
    # ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)
    numbers=numbers.split(" ")
    even,odd=[],[]
    for num in numbers:
        if int(num)%2==0:
            even.append(num)
        else: 
            odd.append(num)
    if len(even)==1:
        return numbers.index(even[0])+1
    else:
        return numbers.index(odd[0])+1

# --------------------------------------------Extras--------------------------------------------

#Other solutions

def iq_test2(numbers):

    #Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.
    # ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)
    e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1
