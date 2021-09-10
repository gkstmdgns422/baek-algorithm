# 다 연결되있다길래 그냥 print(N-1)했는데 맞아버렸다.
import sys

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, sys.stdin.readline().split())
    for _ in range(M):
        V,E = map(int, sys.stdin.readline().split())
    print(N-1)
