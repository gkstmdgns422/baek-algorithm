N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))
sort_lst = sorted(lst)
max_sum = 0
for i in range(N):
    sum_lst = sort_lst[N-1-i] * (i+1)
    if max_sum < sum_lst:
        max_sum = sum_lst
print(max_sum)