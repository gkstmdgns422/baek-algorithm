n, m = map(int, input().split())

fee = [0] + [int(input()) for _ in range(n)]
weight = [0] + [int(input()) for _ in range(m)]
in_out = [int(input()) for _ in range(2*m)]
parking = [0] * (n+1)
queue = []
income = 0
cnt = n
while in_out:
    if cnt and queue:
        car = queue.pop(0)
    else:
        car = in_out.pop(0)

    if car < 0: # 나가는 차량
        area = parking.index(-car)
        parking[area] = 0
        income += fee[area] * weight[-car]
        cnt += 1
    elif car > 0 and not cnt: # 파킹이 꽉차고 추가차량
        queue.append(car)
    else:  # car > 0 이고 cnt가 존재
        i = 1
        while i < n+1:
            if not parking[i]:
                parking[i] = car
                cnt -= 1
                break
            else:
                i += 1
        else:
            queue.append(car)
        
print(income)
        