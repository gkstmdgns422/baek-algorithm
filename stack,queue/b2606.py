def dfs(s):
    visited[s] = 1
    for j in range(1, N+1):
        if node[s][j] and not visited[j]:
            dfs(j)

N = int(input())
C = int(input())
visited = [0] * (N+1)
node = [[0] * (N+1) for _ in range(N+1)]
for _ in range(C):
    V, E = map(int, input().split())
    node[V][E] = node[E][V] = 1 # 컴퓨터 연결은 쌍방향이다.
dfs(1)
print(sum(visited)-1) # 1번 컴퓨터는 비포함 해야하므로 -1
