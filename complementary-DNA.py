"""
Solution to the CodeWars kata Complementary DNA
Link:
https://www.codewars.com/kata/554e4a2f232cdd87d9000038
"""

def DNA_strand(dna):
    #In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all 
    dna_answer=""
    for item in dna:
        if item == "A":
            dna_answer+="T"
        elif item == "T":
            dna_answer+="A"
        elif item == "C":
            dna_answer+="G"
        else:
            dna_answer+="C"
    return dna_answer

# -----------------------------------------------------Extras-----------------------------------------------------
#Other solution
def DNA_strand2(dna):
    #In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all 
    pairs = {'A':'T','T':'A','C':'G','G':'C'}
    return ''.join([pairs[x] for x in dna])

