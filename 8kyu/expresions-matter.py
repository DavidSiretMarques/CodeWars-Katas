"""
Solution to the CodeWars kata Expressions Matter
Link:
https://www.codewars.com/kata/5ae62fcf252e66d44d00008e/python
"""

def expression_matter(a, b, c):
    return max((a+b)*c,a+b+c,a*(b+c),a*b*c )