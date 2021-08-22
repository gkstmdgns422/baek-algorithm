T = int(input())
for _ in range(T):
    between = list(map(str, input().split()))
    a, b = between[0], between[1]
    zero = one = 0
    for i in range(len(a)): # 자릿수만큼 회전
        if a[i] != b[i]:
            if a[i] == '1':
                one += 1
            else:
                zero += 1
     
    cnt = 0
    if zero == one:
        for i in range(len(a)):
            if a[i] == '1' and b[i] == '0':
                cnt += 1          
    elif zero > one:
        for i in range(len(a)):
            if a[i] == '0' and b[i] == '1':
                cnt += 1     
    else:
        for i in range(len(a)):
            if a[i] == '1' and b[i] == '0':
                cnt += 1
    print(cnt)