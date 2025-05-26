"""
Solution to the CodeWars kata Sentence Smash
Link:
https://www.codewars.com/kata/53dc23c68a0c93699800041d
"""
def smash(words):
    text=""
    for i in range(len(words)):
        text+=words[i]
        if i < len(words)-1:
            text+=" "
    return text