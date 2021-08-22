import sys
# 입력 데이터 불러오기
book_num = int(input())
book_list =[int(sys.stdin.readline())]
max_num = book_list[0]

for i in range(1,book_num):
    book_list.append(int(sys.stdin.readline()))
ans = 0
# 처음엔 큰수를 찾고 큰수 앞에 1만큼 작은 수를 찾으려고 코드를 짰으나 시간초과로 인해 초기값부터 진행하는걸로 코드를 만들었습니다.
for i in range(1,book_num): # 처음 수부터 시작
    if book_list[i] > max_num: # 크기 비교 크면 넘기고 작으면 ans에 +1
        if max_num+1 != book_list[i]: # 값 차이가 1이 아니면 ans에 +1
            ans +=1
        max_num = book_list[i] # 값 차이가 1이면 넘긴다.
    else:
        ans +=1
print(ans)



