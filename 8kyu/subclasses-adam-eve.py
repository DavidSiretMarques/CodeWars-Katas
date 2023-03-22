"""
Solution to the kata  Basic Subclasses - Adam and Eve
Link:
https://www.codewars.com/kata/547274e24481cfc469000416/train/python
"""

#Create Human class with a name
class Human:
    def __init__(self,name):
        self.name = name

#Create Man and woman subclasses while assigning a sex
class Man(Human):
    Human.sex = 'Male'
class Woman(Human):
    Human.sex = 'Female'

#Calling the god (create) function to create adam and eve
def God():
    return[Man('Adam'),Woman('Eve')]


print(God())