N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for _ in range(N):
    ans += A.pop(A.index(min(A))) * B.pop(B.index(max(B)))
print(ans)