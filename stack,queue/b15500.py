N = int(input())
ai_1 = list(map(int, input().split())) # 맨밑~맨위
ai_2 = []
# ai_3 = []
sort_ai = sorted(ai_1)
stack = []
# 처음 뽑을때
i = 1
K = 0
while i <= N:
    if sort_ai[N-i] in ai_1: # 1번 장대
        n = ai_1.pop()
        if n == sort_ai[N-i]:
            # ai_3.append(n)
            stack.append([1,3])
            i += 1
        else:
            ai_2.append(n)
            stack.append([1,2])
    elif sort_ai[N-i] in ai_2: # 2번 장대
        n = ai_2.pop()
        if n == sort_ai[N-i]:
            # ai_3.append(n)
            stack.append([2,3])
            i += 1
        else:
            ai_1.append(n)
            stack.append([2,1])
    K += 1

print(K)
for i in range(K):
    print(*stack[i])