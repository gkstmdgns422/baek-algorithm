import sys

N, W = map(int, sys.stdin.readline().split())
node = [0] * (N+1)
for _ in range(N-1):
    U, V = map(int, sys.stdin.readline().split())
    node[U] += 1
    node[V] += 1
cnt = 0
for i in range(2, N+1): # 루트 노드는 제외
    if node[i] == 1: # 부모와 자식만 연결되있다면
        cnt += 1
print(W / cnt)


# 문제 틀림 분석 : 노드가 순차적으로 진행되는것(1,2,3,4,5...)이 아니라 크기 상관없이 루트와 자식으로 나뉘는듯 하다.(간선 방향성을 모른다.)
# import sys

# N, W = map(int, sys.stdin.readline().split())
# tree = {}
# for _ in range(N-1):
#     U, V = map(int, sys.stdin.readline().split())
#     if U > V:
#         U, V = V, U
#     if tree.get(U):
#         tree[U] = tree[U] + [V]
#     else:
#         tree[U] = [V]
# cnt = 0
# for br in tree.keys():
#     for i in tree[br]:
#         if not tree.get(i):
#             cnt += 1

# print(round(W / cnt, 4))

