"""
Solution to the CodeWars kata Pete, The baker
Link:
https://www.codewars.com/kata/525c65e51bf619685c000059
"""

def cakes(recipe, available):
    #Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.
    cakenumber=[]
    for element in recipe:
        if element in available: 
            cakenumber.append (available[element] // recipe[element])
        else: 
            return 0
    return min(cakenumber)
    
# --------------------------------------------Extras--------------------------------------------

#Other solutions
        
def cakes2(recipe, available):
    try:
        return min([available[a]/recipe[a] for a in recipe])
    except:
        return 0
