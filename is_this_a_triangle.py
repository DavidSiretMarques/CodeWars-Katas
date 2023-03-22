from math import sqrt

def is_triangle(a, b, c):
    # Epsilon aka error value aka 0 (but it's not 0 because computers think that 0.000000000001 and 0 are not equal and have finite precission)
    eps = 1e-6   
    p_half = (a + b + c) / 2
    if a < 0 or b < 0 or c < 0 or p_half < a or p_half < b or p_half < c:
        return False
    area = sqrt(p_half*(p_half-a)*(p_half-b)*(p_half-c))
    if  area < eps:
        return False
    return True
