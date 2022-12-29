def solution(n):
    num = 1
    pows = []
    while num <= n:
        pows.append(num)
        num *= 2
    return pows
