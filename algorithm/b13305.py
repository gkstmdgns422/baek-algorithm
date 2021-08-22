# 100점
city = int(input())
roads = list(map(int, input().split()))
oil_price = list(map(int, input().split()))

total = 0
min_price = oil_price[0]
for i in range(city-1):
    if oil_price[i] < min_price:
        min_price = oil_price[i]
    total += min_price * roads[i]
print(total)

# 17점 (기름값이 모두 1일때의 시간복잡도 때문으로 판단)
# min_price = 0
# idx = 0
# while idx < len(roads):
#     if idx == len(roads)-1:
#         min_price += oil_price[idx] * roads[idx]
#         break
#     elif oil_price[idx] <= oil_price[idx+1]:
#         min_price += oil_price[idx] * (roads[idx] + roads[idx+1])
#         idx += 2
#     else:
#         min_price += oil_price[idx] * roads[idx]
#         idx += 1
# print(min_price)