N, K = map(int, input().split())

lst = [k for k in range(1, N+1)]
stack = []
i = K - 1  # i는 lst의 인덱스
while True:
    if i > len(lst)-1:
        i = i-len(lst)
    else:
        stack.append(lst.pop(i))
        i += K - 1
    if len(stack) == N:
        break
word = ''
for j in stack:
    word += str(j) + ', '
print('<{}>'.format(word[:-2]))