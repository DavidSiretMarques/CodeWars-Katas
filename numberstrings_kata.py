"""
Solution to the CodeWars kata Sum Strings as Numbers
Link:
https://www.codewars.com/kata/5324945e2ece5e1f32000370/python
"""


def sum_strings2(num1, num2):
    if num1 == '' and num2 == '':
        return '0'
    elif num1 == '':
        return num2
    elif num2 == '':
        return num1
    else:
        return str(int(num1) + int(num2))


def sum_strings(num1, num2):
    length = max(len(num1), len(num2))
    result = ''
    carry = 0
    num1 = num1.zfill(length)
    num2 = num2.zfill(length)
    for i in range(length-1, -1, -1):
        carry, digit = divmod(int(num1[i]) + int(num2[i]) + carry, 10)
        result += str(digit)
    return ('1' * carry + result[::-1]).lstrip('0') or '0'


if __name__ == '__main__':
    print(sum_strings('7', '7'))  # 14
    print(sum_strings('17', '27'))  # 44
    print(sum_strings('9223372036854775807', '13'))  # 9223372036854775820
