function = input().split('-') 
# -를 기준으로 괄호를 치면 가장 작은수를 출력 할 수 있다.
ans = 0 # 초기값

for first_num in function[0].split('+'): # 초기값 '50+40'와 같은 항목에서 +를 제외
    ans += int(first_num)

for plus_num in function[1:]: # 초기값을 제외한 수는 모두 -를 해야한다.
    for i in plus_num.split('+'):
        ans -= int(i)
print(ans)