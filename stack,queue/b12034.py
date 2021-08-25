# case 1
# 맨 위부터 시작(정가를 뽑아서 계산)
T = int(input())  # 테스트 케이스 수
for tc in range(1, T + 1):
    N = int(input())  # 상품수
    P = list(map(int, input().split())) # 오름차순된 가격리스트
    sale_cost = [] # 세일 가격을 담을 리스트

    while P:
        K = P.pop() # pop()는 마지막 인덱스를 출력 => 정가
        sale = int(K*3/4) # 정가에 0.75배한것 int를해줘야 소수점이 안나온다
        sale_cost.append(sale)
        P.remove(sale)

    print('Case #{}: '.format(tc),end='')
    print(' '.join(map(str, sale_cost[::-1])))

# case 2
# 맨 밑부터 시작(세일된 가격을 뽑아서 계산)
T = int(input())  # 테스트 케이스 수
for tc in range(1, T + 1):
    N = int(input())  # 상품수
    P = list(map(int, input().split())) # 오름차순된 가격리스트
    sale_cost = [] # 세일 가격을 담을 리스트

    while P:
        K = P.pop(0) # 맨 밑을 출력 => 세일된 가격
        cost = K*4//3 # //을 함으로써 정수출력
        sale_cost.append(K)
        P.remove(cost)

    print('Case #{}: '.format(tc), end='')
    print(' '.join(map(str, sale_cost)))