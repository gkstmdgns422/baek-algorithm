# 예시 20,1,15,8,4,10을 받고 정렬을 하면 최종 정렬 리스트는 20,1,15,4,10,8이다.
# 이떄 값을 계산해보면 |20-8|+|1-20|+|15-1|+|4-15|+|10-4| = 62이다.
# 문제가 이해하기 어렵게 되어있어 힘들었다.
N = int(input())
nums = list(map(int, input().split()))
lst = []
max_ans = 0
visited = [0 for _ in range(N)]
def dfs(v):
    global max_ans
    if v == N:
        ans = sum(abs(lst[i]-lst[i-1]) for i in range(N-1))
        if ans > max_ans:
            max_ans = ans
        return
    for idx in range(N):
        if not visited[idx]:
            lst.append(nums[idx])
            visited[idx] = 1
            dfs(v+1)
            visited[idx] = 0
            lst.pop()
        
dfs(0)
print(max_ans)