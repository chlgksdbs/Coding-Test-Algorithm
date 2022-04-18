from collections import deque

# n : 도시의 개수, m : 도로의 개수, k : 거리 정보, x : 출발 도시의 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)] # 0 ~ n까지의 2차원 리스트(빈리스트) 생성, index 0은 사용 X 

for _ in range(m): # 모든 도로 정보 입력받기
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1) # 모든 도시에 대한 최단 거리 초기화
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

q = deque([x]) # 너비 우선 탐색(BFS) 수행
while q: # queue가 빌 때까지 수행
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1: # 아직 방문하지 않은 도시라면,
            distance[next_node] = distance[now] + 1 # 최단 거리 갱신
            q.append(next_node)

check = False
for i in range(1, n + 1): # 최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
    if distance[i] == k:
        print(i)
        check = True

if check == False: # 만약 최단 거리 k인 도시가 없다면,
    print(-1)
