T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = {}
    for _ in range(N-1):
        A, B = map(int, input().split()) 
        tree[B] = A # 딕셔너리에 존재하는지 확인 (자식 : 선조) 로 저장
    C, D = map(int,input().split())
    ancestor = [C, D]
    lst = [C, D]
    while ancestor:
        node = ancestor.pop(0)
        if node in tree:
            num = tree[node]
            if num in lst:
                print(num)
                break
            else:
                lst.append(num)
                ancestor.append(num)
        else:
            continue
        