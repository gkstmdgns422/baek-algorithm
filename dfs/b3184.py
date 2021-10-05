import sys
sys.setrecursionlimit(1000000)

R, C = map(int, input().split())

yard = [list(input()) for _ in range(R)]
visited = [[0] * (C) for _ in range(R)]
for i in range(R):
    for j in range(C):
        if yard[i][j] == '#':
            visited[i][j] = 1
sheep = wolf = 0
s_cnt = w_cnt = 0
dx = [1,-1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    global sheep, wolf
    visited[x][y] = 1
    if yard[x][y] == 'o':
        sheep += 1
    elif yard[x][y] == 'v':
        wolf += 1
    
    for i in range(4):
        now_x, now_y = x+dx[i], y+dy[i]
        if 0 <= now_x < R and 0 <= now_y < C and not visited[now_x][now_y]:
            dfs(now_x, now_y)
    

for i in range(R):
    for j in range(C):
        if not visited[i][j]:
            dfs(i, j)
            if wolf >= sheep:
                w_cnt += wolf
            else:
                s_cnt += sheep
            sheep = wolf = 0
print('{} {}'.format(s_cnt, w_cnt))
    
    