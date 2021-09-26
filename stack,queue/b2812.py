N, K = map(int, input().split())
nums = list(map(int, input()))
cnt = K
queue = []
for i in range(N):
    while queue and K > 0:
        if queue[-1] < nums[i]:
            queue.pop()
            K -= 1
        else:
            break
    queue.append(nums[i])
    if len(queue) == N-cnt+1:
        for num in range(len(queue)-1):
            print(queue[num], end='')
        break
else:
    for num in queue:
        print(num, end='')

# num = nums[:K]
# nums = nums[K:]
# # 맨앞자리수
# cnt = num.index(max(num))
# num = num[cnt:]
# K -= cnt
#
# nums = num + nums
# # 그 다음 자리수들
# idx = count = 0
# while K > 0:
#     if nums[idx] >= nums[idx+1]:
#         idx += 1
#         count += 1
#     elif nums[idx] < nums[idx+1]:
#         nums.pop(idx)
#         K -= 1
#     if count == len(nums) - K:
#         nums = nums[:idx]
#         break

