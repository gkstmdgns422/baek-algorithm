price = int(input()) # 물건 가격
 
change = 1000 - price # 거스름돈
change_wallet = [500,100,50,10,5,1] # 거스름돈 종류
count = 0 # 거스름돈 개수
for i in change_wallet:
    if change // i >= 1:
        count += change // i # 거스름돈 갯수 더하기
        change = change % i # 거스름돈 나머지
if change == 0:
    print(count)