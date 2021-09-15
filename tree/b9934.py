K = int(input())
nums = list(map(int, input().split()))
# 맨밑 : 2, 그위 : 4, 그위 : 8, 그위 : 16

tree = []

for j in range(K):
    tree.append([nums[i] for i in range(2**j-1,2**K-1,2**(j+1))])

for k in tree[::-1]:
    print(*k)

    
