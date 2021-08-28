def bfs(s):
    queue = []
    queue.append(s)
    visited[s] = 1
    while queue:
        t = queue.pop(0)
        for i in range(1, n+1):
            if not visited[i] and lst[t][i]:
                queue.append(i)
                visited[i] = visited[t] + 1  # 그래프 순서 표시


n = int(input())
num1, num2 = map(int, input().split())
m = int(input())
lst = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)
for i in range(m):
    x, y = map(int, input().split())
    lst[x][y] = lst[y][x] = 1  # 쌍방향 이여야 하므로 표시

bfs(num1)

if visited[num2]: # 방문 가능 여부 확인
    print(visited[num2]-1)
else:
    print(-1)
