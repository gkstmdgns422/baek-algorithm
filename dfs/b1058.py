N = int(input())

matrix = [list(input()) for _ in range(N)]
person = [0 for _ in range(N)]

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'Y':  # 서로 친구인 경우
            person[i] += 1
        elif i != j and matrix[i][j] == 'N':  # 서로 친구가 아닌경우
            for u in range(N):
                if matrix[u][i] == matrix[u][j] == 'Y':  # 서로 아는 친구가 존재할 경우
                    person[i] += 1
                    break

print(max(person))

