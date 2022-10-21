
"""
Solution to the CodeWars kata Array.diff
Link:
https://www.codewars.com/kata/523f5d21c841566fde000009
"""
def array_diff(a, b):
    #Function that eliminates the items in list b from the list a
    for item in b:
        if item in a:
            while item in a:
                a.remove(item)
    return a
