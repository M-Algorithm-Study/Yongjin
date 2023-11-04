# 네트워크 연결

import sys
sys.stdin = open('input.txt','r')

# 크루스칼

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 떄까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
M = int(input())
# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
parent = [0] * (N+1)
edges = []
result = 0

#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, N+1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력 받기
for _ in range(M):
    a,b,cost = map(int,input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost,a,b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a , b = edge
    # 사이클이 발생하지 않는 경우에마 집합에 포함
    if find_parent(parent, a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)


# # 프림
# import heapq

# n = int(input())
# m = int(input())

# graph = [[] for _ in range(n+1)]
# visited = [ False for _ in range(n+1)]
# answer = 0

# for i in range(m):
#     a,b,c = map(int,input().split())
#     graph[a].append((c,b))
#     graph[b].append((c,a))

# # 각각의 번호에 들어가는 수
# # [[], [(5, 2), (4, 3)], [(5, 1), (2, 3), (7, 4)], [(4, 1), (2, 2), (6, 4), (11, 5)], [(7, 2), (6, 3), (3, 5), (8, 6)], [(11, 3), (3, 4), (8, 6)], [(8, 4), (8, 5)]]

# queue = []
# # 큐의 초기값
# heapq.heappush(queue, (0,1))

# def prim():
#     global answer
#     while queue:
#         wei, now = heapq.heappop(queue)
#         if visited[now] == False:
#             visited[now] = True
#             answer += wei
#             for next_wei, next_node in graph[now]:
#                 heapq.heappush(queue, (next_wei,next_node))
#     return answer

# print(prim())

