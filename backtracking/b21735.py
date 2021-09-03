N, M = map(int, input().split())
a = [0] + list(map(int, input().split()))

max_ans = 0

def dfs(v,ans, cnt): # v=시작지점, ans=눈덩이크기, cnt=시간
    global max_ans
    if cnt > M: # 시간 초과시
        return
    else:
        if max_ans < ans: # 계속 진행가능하다면 max값 구하기
            max_ans = ans
    if v <= N-1: # 인덱스 초과 발생하여 추가한 상황
        dfs(v+1, ans + a[v+1], cnt+1)
    if v <= N-2: # 인덱스 초과 발생하여 추가한 상황
        dfs(v+2, ans//2 + a[v+2], cnt+1)
dfs(0,1,0)
print(max_ans)