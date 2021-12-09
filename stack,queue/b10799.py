# lst = list(input())
# queue = 0
# cnt = 0
# result = 0
# for idx, val in enumerate(lst):
#     if val == '(':
#        cnt += 1
#        queue += 1
#     elif val == ')' and lst[idx-1] == '(': # 레이져
#         cnt -= 1
#         queue -= 1
#         result += cnt
#     else:
#         cnt -= 1
#         result += 1
#     if not queue:
#         cnt = 0
# print(result)

lst = list(input())
cnt = 0
result = 0
for idx, val in enumerate(lst):
    if val == '(':
       cnt += 1
    elif val == ')' and lst[idx-1] == '(': # 레이져
        cnt -= 1
        result += cnt
    else:
        cnt -= 1
        result += 1
print(result)
        