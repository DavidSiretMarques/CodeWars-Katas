"""
Solution to the CodeWars kata Tribonacci sequence
Link:
https://www.codewars.com/kata/556deca17c58da83c00002db/python
"""

def tribonacci(signature, n):
    #Gives the tribonacci sequence (adding the 3 previous numbers) up to n numbers
    tribonacci_seq=[]
    if n==0:
        return tribonacci_seq
    for i in range(0,n):
        if i<3:
            tribonacci_seq.append(signature[i])
        else:
            tribonacci_seq.append(tribonacci_seq[i-1]+tribonacci_seq[i-2]+tribonacci_seq[i-3])
    return tribonacci_seq 


#--------------------------------------------------Extras--------------------------------------------------

def tribonacci_num(n):
    #Calculates the number n of the tribonacci sequence (adds the 3 previous numbers)
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        return tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)
   
def tribonacci2(signature, n):
    #Gives the tribonacci sequence (adding the 3 previous numbers) up to n numbers (other solution)
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res

def fibonacci_num(n):
    #Calculates the number n of the fibonacci sequence
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci_num(n-1)+fibonacci_num(n-2)


def fibonacci(n):
    #Gives the fibonacci sequence up to the n-th element
    fib_seq = [0]
    if n == 0:
        return fib_seq
    for i in range(n):
        if i < 1:
            fib_seq.append(1)
        else:
            fib_seq.append(fib_seq[i-1]+fib_seq[i])
    return fib_seq

