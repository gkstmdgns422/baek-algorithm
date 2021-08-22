import sys
T = int(input())

account = []
for i in range(T):
    money = int(sys.stdin.readline())
    # 장부에 돈 기입 or 삭제
    if money:
        account.append(money)
    else:
        account.pop() # pop의 괄호안에 숫자가 없으면 맨 마지막수 삭제
    
# 장부에 적힌 돈의 최종합
total = 0

for m in account:
    total += m
print(total)
