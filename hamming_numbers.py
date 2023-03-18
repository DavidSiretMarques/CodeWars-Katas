"""
Solution for the hamming numbers kata

Available in:
https://www.codewars.com/kata/526d84b98f428f14a60008da/train/python
"""


def hamming(limit):
    h = [1] * limit
    x2, x3, x5 = 2, 3, 5
    i = j = k = 0

    for n in range(1, limit):
        h[n] = min(x2, x3, x5)
        if x2 == h[n]:
            i += 1
            x2 = 2 * h[i]
        if x3 == h[n]:
            j += 1
            x3 = 3 * h[j]
        if x5 == h[n]:
            k += 1
            x5 = 5 * h[k]

    return h


if __name__ == '__main__':
    print([1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36, 40, 45, 48, 50, 54, 60, 64, 72, 75,
           80, 81, 90, 96, 100, 108, 120, 125, 128, 135, 144, 150, 160, 162, 180, 192, 200, 216, 225, 240, 243])
    print(hamming(50))
