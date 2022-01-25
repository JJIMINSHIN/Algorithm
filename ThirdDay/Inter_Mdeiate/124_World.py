def solution(n):
    result = ''
    while n != 0:
        if n % 3 != 0:
            result += str(n % 3)
            n //= 3
        elif n % 3 == 0:
            result += "4"
            n //= 3; n -= 1
    return result[::-1]