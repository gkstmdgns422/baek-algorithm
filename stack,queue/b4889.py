
flag = 1
tc = 0
while flag:
    lst = list(input())
    result = 0
    right = 0
    left = 0
    if '-' not in lst:
        for idx, val in enumerate(lst):
            if val == '}' and left:
                left -= 1
            elif val == '}' and not left:
                right += 1
            elif val == '{':
                left += 1
        if right%2 or left%2: # 홀수인 경우
            result += (right//2 + left//2 + 2)
        else:
            result += (right//2 + left//2)

        tc += 1
        print(f'{tc}. {result}')  
    else:
        flag = 0
