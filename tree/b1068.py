N = int(input())
tree = {}
r_node = list(map(int, input().split())) 
del_node = int(input())
leaf_cnt = 0

for idx in range(N):
    if idx == del_node or r_node[idx] == del_node: # 삭제되는 노드 혹은 삭제되는 노드의 자식 노드라면 필요없음
        continue
    if r_node[idx] in tree: # 딕셔너리에 존재하는지 확인
        tree[r_node[idx]].append(idx) 
    else: # 없다면
        tree[r_node[idx]] = [idx]

if -1 in tree: # 맨상위루트가 딕서녀리에 존재하는지
    queue = [-1]
else: # del_node == -1이라면 값은 0이므로 queue리스트는 빈리스트이다.
    queue = []
while queue: # 한개씩 빼가면서 자식노드를 확인하는 방법
    node = queue.pop() # node = -1 , tree = {-1:[1,2]}
    if node not in tree: # tree[node] 가 존재하는지
        leaf_cnt += 1
    else:
        queue += tree[node]

print(leaf_cnt)
