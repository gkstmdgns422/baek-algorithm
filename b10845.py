import sys
T = int(input())

queue = []
for tc in range(T):
    lst = sys.stdin.readline().split()
    if lst[0] == 'push':
            queue.append(lst[1])

    elif lst[0] == "pop":
        if len(queue): 
            print(queue.pop(0))
        else: 
            print(-1)

    elif lst[0] == "size":
        print(len(queue))

    elif lst[0] == "empty":
        if len(queue): 
            print(0) 
        else: 
            print(1)

    elif lst[0] == "front":
        if len(queue):
            print(queue[0])
        else: 
            print(-1)

    elif lst[0] == "back":
        if len(queue): 
            print(queue[-1])
        else: 
            print(-1)