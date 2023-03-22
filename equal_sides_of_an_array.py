"""
Solution to the CodeWars kata Equal Sides of an array
Link:
https://www.codewars.com/kata/5679aa472b8f57fb8c000047/python
"""
def find_even_index(arr):
    index = 0
    while sum(arr[:index]) != sum(arr[index+1:]):
        index +=1
        if index >= len(arr):
            return -1
    return index
   
   
if __name__=='__main__':
    print(find_even_index([1,2,3,4,3,2,1]))
    