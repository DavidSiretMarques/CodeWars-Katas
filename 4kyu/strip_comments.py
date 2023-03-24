"""
Solution for the CodeWars kata Strip Comments

Available in:
https://www.codewars.com/kata/51c8e37cee245da6b40000bd
"""
import re


def strip_comments(strng, markers):
    # Join the markers as a string and escape the -
    str_markers = ''.join(markers).replace('-', '\-')
    pattern = '\t? *[(' + str_markers + ')].*'
    if len(markers) >= 1:
        strng = re.sub(pattern, '', strng)
    return strng


if __name__ == '__main__':
    print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))
