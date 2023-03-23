"""
Solution to the CodeWars kata Count the smiley faces!
Link:
https://www.codewars.com/kata/583203e6eb35d7980400002a
"""


def count_smileys(arr):
    eyes = [':', ';']
    nose = ['-', '~']
    mouth = [')', 'D']
    smiley_count = 0
    for smiley in arr:
        if 1 < len(smiley) <= 3:
            if len(smiley) == 3:
                if smiley[0] in eyes and smiley[1] in nose and smiley[2] in mouth:
                    smiley_count += 1
            elif smiley[0] in eyes and smiley[-1] in mouth:
                smiley_count += 1
    return smiley_count


