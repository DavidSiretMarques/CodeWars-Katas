"""
Solution to the CodeWars kata Simple Pig Latin
Link:
https://www.codewars.com/kata/520b9d2ad5c005041100000f
"""
def pig_it(text):
    #Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
    textlist=text.split(" ")
    result=[]
    for item in textlist:
        if (item.find("!") and item.find("?"))==(-1):
            result.append(item[1:]+item[:1]+"ay")
        else:
            result.append(item)
    return (" ").join(result)

# --------------------------------------------Extras--------------------------------------------

#Other solutions

def pig_it2(text):
    #Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
