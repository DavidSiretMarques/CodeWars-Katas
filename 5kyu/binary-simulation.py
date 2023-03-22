"""
Solution to the CodeWars kata Binary Simulation
Link:
https://www.codewars.com/kata/5cb9f138b5c9080019683864
"""

def binary_simulation(s, q):
    output, num, st = [],int(s,2),len(s)
    for cmd,*i in q:
        if cmd=='I':
            start,end=i
            num ^= (1<<end-start+1)-1<<st-end
        else:
            output.append( str(int(0 < 1<<(st-i[0]) & num)) )
    return output

if __name__ == "__main__":
    print (binary_simulation("0011001100", [['I', 1, 10], ['I', 2, 7], ['Q', 2], ['Q', 1], ['Q', 7], ['Q', 5]]))
    