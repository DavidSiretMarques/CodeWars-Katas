"""
Solution to the kata Stop gninnipS My sdroW!  in codewars
Link:
https://www.codewars.com/kata/5264d2b162488dc400000001/python
"""

def spin_words(sentence):
    sentence = sentence.split(" ")
    s = []
    for word in sentence:
        if len(word)>=5:
            w = ''
            for i in reversed(range(len(word))):
                w += word[i]
            word = w
        s.append(word)
    # Your code goes here
    return ' '.join(s)

print(spin_words('Welcome'))

# --------------------------------------------Extras--------------------------------------------

#Other solutions

def spin_words(sentence):
    #Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
    res=[]
    words=sentence.split()
    for item in words:
        if len(item)>=5:
            item = item [::-1]
            res.append(item)
        else:
            res.append(item)
    return " ".join(res)

def spin_words2(sentence):
    #Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
