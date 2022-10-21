"""
Solution to the CodeWars kata Directions Reduction
Link:
https://www.codewars.com/kata/550f22f4d758534c1100025a/python
"""

def dirReduc(arr):
    print(arr)
    dir={"NORTH":"SOUTH", "SOUTH":"NORTH", "EAST":"WEST", "WEST":"EAST"}
    i=0
    while i+1<len(arr):
        if dir[arr[i]]==arr[i+1]:
            del arr[i]
            del arr[i]
            i=0
        else: 
            i+=1
    return arr

def dirReduc2(plan):
    opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan
