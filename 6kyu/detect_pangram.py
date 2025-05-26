"""
Solution to the CodeWars kata Detect Pangram
Link:
https://www.codewars.com/kata/545cedaa9943f7fe7b000048
"""
def is_pangram(st):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    sentence= ''.join(st.lower())
    pangram=[(sentence.find(letter) != -1) for letter in alphabet]
    return False if False in pangram else True