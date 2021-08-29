def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1): # 그 수의 루트만큼만 계산
        if num % i == 0:
            return False
    return True

def dfs(num):
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(10): # 0부터 9까지 숫자들
            cnt = num*10 + i # [2,3,5,7] * 10 + 1~9숫자들
            if prime(cnt): # 더한 숫자가 소수라면? 다시 dfs반복
                dfs(cnt)

n = int(input()) # 자릿수
first = [2,3,5,7] # 맨위자릿수가 2,3,5,7이여야 하므로
for num in first:
    dfs(num)

# 메모리 초과 : 에라토스테네스의 체를 사용하면 메모리 초과가 발생
# n = int(input())
# a = [False,False] + [True] * (10**n-1)
# primes = []

# def prime(n):
#     if n < 2:
#         return
#     for i in range(2, n+1):
#         if a[i]:
#             primes.append(i)
#         for j in range(2*i, n+1, i):
#             a[j] = False

# prime(10**n)

# for num in primes:
#     k = len(str(num))
#     cnt = 0
#     if k == n:
#         for i in range(1, k):
#             if i == k-1:
#                 if num//10**i in [2,3,5,7]:
#                     cnt += 1
#             elif num//10**i in primes:
#                 cnt += 1
#         if cnt == k-1:
#             print(num)









