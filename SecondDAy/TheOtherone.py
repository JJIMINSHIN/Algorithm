
def solution(n):
    answer = 0
    for i in range(3, n):
        if n % i  == 1:
            return i
    return answer