A, B = map(int,input().split())
cnt = 1               # 최소값에 1을 더한값을 구해야하므로 cnt는 1부터 시작

while True:
    if B == A:        # 진행하며 B와 A가 같아지면 스탑
        print(cnt)
        break
    elif B < A:       # B가 A보다 작아지게 되면 구할필요 없으므로 스탑
        print(-1)
        break
    if B % 2:         # 홀수
        if B%10 == 1: # 1의 자리가 1인경우
            B //= 10 
            cnt += 1
        else:         # 1의 자리가 1이 아니면 진행 필요X
            print(-1)
            break
    else:             # 짝수
        B //= 2 
        cnt += 1
    
