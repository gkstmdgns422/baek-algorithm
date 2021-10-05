import sys
sys.setrecursionlimit(1000000)

def dfs(s,e,val):
    visited[s][e] = 1
    for i in range(4):
        nx, ny = s+dx[i], e+dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if picture[nx][ny] == val:
                dfs(nx, ny, val)

def change():
    global picture
    for x in range(N):
        for y in range(N):
            if picture[x][y] == 'G':
                picture[x][y] = 'R'

N = int(input())
picture = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

cnt = cb_cnt = 0
for u in range(N):
    for v in range(N):
        if not visited[u][v]:
            dfs(u,v,picture[u][v])
            cnt += 1
            
change()
visited = [[0] * N for _ in range(N)]


for u in range(N):
    for v in range(N):
        if not visited[u][v]:
            dfs(u,v,picture[u][v])
            cb_cnt += 1

print(cnt, cb_cnt)

        