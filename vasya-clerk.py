"""
Solution to the CodeWars kata Vasya-Clerk
Link:
https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8
"""

def tickets(people):
    #Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?
    #Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.
    cash25=0
    cash50=0
    cash100=0
    for money in people:
        if money ==25:
            cash25+=1
        elif money== 50:
            if cash25>=1:
                cash50+=1
                cash25-=1
            else:
                return "NO"
        else:
            cash100+=1
            if cash50>=1 and cash25>=1:
                cash25-=1
                cash50-=1
            elif cash25>=3:
                cash25-=3
            else:
                return "NO"
    return "YES"       

# --------------------------------------------Extras--------------------------------------------

#Other solutions

def tickets2(people):
    #Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?
    #Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.
  till = {100.0:0, 50.0:0, 25.0:0}

  for paid in people:
    till[paid] += 1
    change = paid-25.0
    
    for bill in (50,25):
      while (bill <= change and till[bill] > 0):
        till[bill] -= 1
        change -= bill

    if change != 0:
      return 'NO'
        
  return 'YES'
