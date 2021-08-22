import sys

book_num = int(input())
book_list =[int(sys.stdin.readline())]
for i in range(1,book_num):
    book_list.append(int(sys.stdin.readline()))

max_num = max(book_list)
max_idx = book_list.index(max_num)
ans = max_num - 1

for i in range(ans,-1,-1):
    if book_list.index(max_num-1) > max_idx:
        print(ans)
    else:
        max_idx = book_list.index(max_num-1)
        ans -= 1   
print(ans)


