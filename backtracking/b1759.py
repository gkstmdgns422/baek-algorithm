import sys
sys.setrecursionlimit(10000)
def dfs(v, v_cnt, w_cnt):
    global words
    if v_cnt >= 1 and w_cnt >= 2 and len(words) == L:
        print(''.join(words))
        return
    for i in range(v,C):
        if not use[i]:
            words.append(word[i])
            use[i] = 1
            if word[i] in 'aeiou':
                dfs(i+1,v_cnt+1,w_cnt)
            else:
                dfs(i+1,v_cnt,w_cnt+1)
            words = words[:-1]
            use[i] = 0

L, C = map(int, input().split())
word = list(input().split())
word.sort()
use = [0 for _ in range(C)]
words = []
dfs(0,0,0)


