import sys

book_num = int(input())
book_list =[int(sys.stdin.readline())]
max_num = book_list[0]

for i in range(1,book_num):
    book_list.append(int(sys.stdin.readline()))
ans = 0

for i in range(1,book_num): 
    if book_list[i] > max_num:
        if max_num+1 != book_list[i]:
            ans +=1
        max_num = book_list[i]
    else:
        ans +=1
print(ans)



