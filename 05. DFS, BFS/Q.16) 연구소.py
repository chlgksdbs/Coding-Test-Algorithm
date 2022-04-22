from collections import deque
from itertools import combinations
import copy # 리스트의 깊은 복사(내부에 객체들까지 모두 새롭게 copy)를 위한 라이브러리

def bfs(graph, v):
    count = 0 # 안전 영역의 크기를 세서 저장하는 변수
    q = deque()
    for i in range(len(v)): # 바이러스가 존재하는 구역을 모두 queue에 삽입
        q.append([v[i][0], v[i][1]])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q: # 큐가 빌 때까지 수행
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 1: # 범위를 벗어나거나, 해당 칸이 벽이면 무시
                continue

            if graph[nx][ny] == 0: # 해당 칸이 빈칸이면 바이러스로 변환시키고, queue에 삽입
                graph[nx][ny] = 2
                q.append([nx, ny])
    
    for i in range(n): # 바이러스를 모두 퍼뜨린 후, 안전 영역의 크기 계산
        count += graph[i].count(0)
    
    return count

n, m = map(int, input().split()) # n : 세로 크기, m : 가로 크기
graph = [] # 지도의 모양을 담을 리스트
for _ in range(n): # 0 : 빈칸, 1 : 벽, 2 : 바이러스
    graph.append(list(map(int, input().split())))

max_value = 0 # 안전 영역의 최대 크기를 저장하는 변수
v_data = [] # 바이러스가 있는 곳의 좌표를 저장할 리스트
b_data = [] # 빈칸인 곳의 좌표를 저장할 리스트

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2: # 바이러스 좌표
            v_data.append([i, j])
        
        elif graph[i][j] == 0: # 빈칸 좌표
            b_data.append([i, j])    

for x, y, z in list(combinations(b_data, 3)): # 빈칸인 좌표에 벽을 세워보는 모든 경우의 수
    temp = copy.deepcopy(graph) # graph 리스트를 깊은 복사를 통해 temp에 복사
    
    # combinations 함수를 통해 뽑은 3개의 빈칸 좌표에 벽을 세움
    temp[x[0]][x[1]] = 1
    temp[y[0]][y[1]] = 1
    temp[z[0]][z[1]] = 1
    
    if max_value < bfs(temp, v_data): # 최대 안전 영역의 크기를 구함
        max_value = bfs(temp, v_data)

print(max_value)

'''
* 새롭게 알게된 개념

- 얕은 복사(shallow copy)
- 깊은 복사(deep copy)

위 코드의 51번째 line에서 list의 얕은 복사를 했을 때, temp에 graph를 할당하면 값이 할당되는 것이 아니라 같은 메모리 주소를 바라본다.
따라서 서로 같은 메모리 주소를 바라보기 때문에 graph 값을 변경하면 temp가 바뀌고, temp 값을 변경하면 graph가 바뀐다.
위와 같이 mutable한 객체간에는 깊은 복사를 해야한다.
'''
