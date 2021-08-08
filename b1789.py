total = int(input()) # S
N = 1 # 자연수 1부터 시작
# 문제의 원하는 바는 1부터~최대N까지의 합이 S보다 작을때의 최대값N을 찾는것!
while total >= 0:
    total -= N 
    N += 1
print(N-2) # 2를 빼는 이유는 마지막에 1을 더해주기 때문에 2를 뺀다.


