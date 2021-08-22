'''
3개 버튼 시간이 300, 60, 10에서
최소 공배수는 300, 최대 공약수는 10 이다
따라서 300,60,10순으로 나눠 그 몫을 각각 구하는게 현명하다라고 생각
'''
time = int(input())

a = time//300 
time %= 300
b = time//60
time %= 60
c = time//10
if time%10:
    print(-1)
else:
    print(a,b,c)
