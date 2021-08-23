import math

N = int(input())
# 출력 값을 확인해보면 2^n - x => 2^n - 2*x임을 알 수 있다.
n = math.ceil(math.log2(N))
x = 2**n - N
print(2**n - 2 * x)
    


# 시간초과 : N이 50만까지 주어지기 때문에 시간복잡도를 낮출 필요가 있다.
# card = [i for i in range(N,0,-1)]
# while len(card) > 1:
#     card.pop() # 맨위 카드 버리기
#     card.insert(0, card.pop()) # 맨위 카드 맨 아래로 옮기기
# print(*card)
