"""
Solution to the CodeWars kata Social Golfer Problem Validator
Link:
https://www.codewars.com/kata/556c04c72ee1147ff20000c9
"""

def valid(a):
    #Write a function that validates a proposed solution, a list of list of strings, as being a solution to the social golfer problem. Each character represents a golfer, and each string is a group of players. Rows represent days. The solution above would be encoded as:
    #You need to make sure (1) that each golfer plays exactly once every day, (2) that the number and size of the groups is the same every day, and (3) that each player plays with every other player at most once.
    day0=("").join(a[0])
    for di in range(len(a)):
        day=("").join(a[di])
        for item in day0:
            #Check for repeated or changed (unknown) players, also checks, by checking the number of times each player appears, the lenght of each day and group
            numberplayedday= day.count(item)
            if numberplayedday!=1:
                return False
            for gi in range(len(a[di])):
                #Find each player in the rest of the days, and check if he repeats mates
                group=[]
                for li in range(len(a[di][gi])):
                    group.append(a[di][gi][li])
                for dayindex in range(len(a)):
                    for groupindex in range(len(a[dayindex])):
                        counter=0
                        if dayindex==di and groupindex==gi:
                            continue
                        for letter in a[dayindex][groupindex]:
                            if letter in group:
                                counter+=1
                            if counter>=2:
                                return False
    return True

