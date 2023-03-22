"""
Solution to the CodeWars kata Are they the "same"?
Link:
https://www.codewars.com/kata/550498447451fbbd7600041c/python
"""

def comp(a, b):
    #Given two arrays a and b write a function comp(a, b) that checks whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
    if isinstance(a,list) and isinstance(b,list):
        if len(a)== len(b):    
            for i in a:
                if a.count(i)!=b.count(i*i):
                    return False
            return True
        else:
            return False
    else:
        return False

# --------------------------------------------Extras--------------------------------------------

#Other solutions

def comp2(array1, array2):
    #Given two arrays a and b write a function comp(a, b) that checks whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False

