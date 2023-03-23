"""
Solution to the CodeWars kata Ball Upwards
Link:
https://www.codewars.com/kata/566be96bb3174e155300001b
"""


def max_ball(v0):
    v, g = v0*1000/3600, 9.81
    h_prev = t = h = 0
    # Check if velocity is positive (negative velocities mean no max height)
    if v0 <= 0:
        return 0
    while h_prev <= h:
        t += 1
        h_prev, h = h, v*t/10 - 0.5*g*t/10*t/10
        # Guard clause to avoid infinite loop for very fast balls
        if t > 1000:
            break
    return t-1


if __name__ == '__main__':
    print(max_ball(37))
