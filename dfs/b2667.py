def dfs(u,v):
    global cnt
    home[u][v] = 0
    cnt += 1
    for i in range(4):
        y, x = u+dx[i], v+dy[i]
        if 0 <= x < N and 0 <= y < N and home[y][x]:
            dfs(y,x)
    return cnt
    

N= int(input())
home = [list(map(int,list(input()))) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
area = []
for u in range(N):
    for v in range(N):
        if home[u][v]:
            cnt = 0
            dfs(u,v)
            area.append(cnt)

area.sort()
print(len(area))
for house in area:
    print(house)
