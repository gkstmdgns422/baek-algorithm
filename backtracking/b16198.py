N = int(input())
nums = list(map(int,input().split()))
max_ans = 0

def dfs(ans):
    global max_ans
    if len(nums) == 2:
        max_ans = max(max_ans,ans)
        return
    for i in range(1,len(nums)-1):
        ans += nums[i-1] * nums[i+1]
        a = nums.pop(i)
        dfs(ans)
        nums.insert(i,a)
        ans -= nums[i-1] * nums[i+1]
        
dfs(0)
print(max_ans)
        
