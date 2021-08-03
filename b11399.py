people_num = int(input())
time = input()

# 리스트로 형변환
time = list(map(int,time.split())) 
# 오름차순 정렬
time.sort()
# 인출하는데 걸리는 시간의 합구하기
total = 0
for i in range(people_num+1):
    total += sum(time[:i]) 
print(total)