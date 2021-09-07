while True:
    k = list(map(int, input().split()))
    if k[0] == 0:
        break
    count = k[0]
    nums = k[1:]
    nums.sort()
    lst = []
    visited = [0 for _ in range(count)]

    def dfs(v, cnt):
        if cnt == 6:
            print(*lst)
            return
        for i in range(v,count):
            lst.append(nums[i])
            visited[i] = 1
            dfs(i+1,cnt+1)
            visited[i] = 0
            lst.pop()

    dfs(0,0)
    print()
