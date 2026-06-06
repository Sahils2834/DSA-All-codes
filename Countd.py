def countDigits(n):
    cnt = 0
    while n > 0:
        cnt = cnt + 1
        n = n // 10
    return cnt