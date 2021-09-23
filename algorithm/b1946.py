import sys

T = int(input())
for tc in range(T):
    N = int(input())
    recruit = [] 
    for i in range(N):
        D, M = map(int, sys.stdin.readline().split())
        recruit.append([D,M])
    p = 0
    recruit.sort()
    fst = recruit[0][1]
    for j in recruit:
        if j[1] <= fst:
                p += 1
                fst = j[1]

    print(p)


# 시간초과 for문을 두번사용해서 완전검색을 사용했기에 그런듯하다.
# import sys

# T = int(input())
# for tc in range(T):
#     N = int(input())
#     recruit = [] 
#     for i in range(N):
#         D, M = map(int, sys.stdin.readline().split())
#         recruit.append([D,M])
#     p = 0
#     for j in recruit:
#         cnt = 0
#         for k in recruit:
#             if j[0] < k[0] or j[1] < k[1]:
#                 cnt += 1
#         if cnt == N-1:
#             p += 1
#     print(p)
