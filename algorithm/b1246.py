N, M = map(int, input().split())
P = list(int(input()) for _ in range(M))
P.sort(reverse=True)
max_price = 0

for idx, price in enumerate(P):
    if idx+1 <= N:
        if (idx+1)*price > max_price:
            max_price = (idx+1)*price
            p = price
    else:
        break
print(p, max_price)
    
