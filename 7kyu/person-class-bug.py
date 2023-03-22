"""
Solution to the CodeWars kata Person Class Bug
Link:
https://www.codewars.com/kata/513f887e484edf3eb3000001/python
"""


class Person():
  
    def __init__(self, first_name, last_name, age):
        self.full_name = first_name + " " + last_name
        self.age = age