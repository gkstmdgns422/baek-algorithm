import sys
N = sys.stdin.readline().rstrip()
stack = []
ans = 1
try:
    for pa in N:
        if pa in ['(','[']:
            stack.append(pa)

        elif pa == ')':
            if stack[-1] == '(': # 바로 괄호가 닫히는지 확인.
                stack.pop()
                stack.append(2)
            else: # 괄호가 안닫힌 경우 이므로 곱셈 적용
                t = 0
                while stack: # 열린괄호가 있는지 확인
                    K = stack.pop() # 열린괄호 pop
                    if K == '(':
                        stack.append(2 * t)
                        break # 괄호가 닫혔으므로 break문 실행
                    elif K == '[':
                        ans = 0
                        break
                    else: # 숫자인 경우
                        t += K

        elif pa == ']':
            if stack[-1] == '[': # 바로 괄호가 닫히는지 확인
                stack.pop()
                stack.append(3)
            else: # 괄호가 안닫힌 경우 이므로 곱셈 적용
                t = 0
                while stack: # 열린괄호가 있는지 확인
                    K = stack.pop() # 열린괄호 pop
                    if K == '[':
                        stack.append(3 * t)
                        break # 괄호가 닫혔으므로 break문 실행
                    elif K == '(':
                        ans = 0
                        break
                    else: # 숫자인 경우
                        t += K
        else: #이상한게 있다?
            ans = 0
            break
    if stack not in ['(','['] and ans: # stack에 열린괄호가 쌓인경우, ans = 0인 경우 고려
        print(sum(stack))
    else:
        print(0)
except: # 문자열과 숫자의 합이 될경우(type에러)
    print(0)
