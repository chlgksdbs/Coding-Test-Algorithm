from collections import deque # BFS에서의 queue를 활용하기 위한 라이브러리

n, m = map(int, input().split()) # n, m 입력
graph = [] # n X m 크기의 미로를 표현하기 위한 리스트
for i in range(n):
    graph.append(list(map(int, input()))) # 띄어쓰기 없이 m만큼의 크기의 수를 입력

dx = [1, -1, 0, 0] # x 이동
dy = [0, 0, 1, -1] # y 이동

def bfs(x, y):
    queue = deque()
    queue.append((x, y)) # 큐에 데이터를 넣을 때 x, y값을 한 쌍으로 삽입
    while queue: # queue가 빌 때까지 수행
        x, y = queue.popleft()
        for i in range(4): # 현재 위치에서 네 방향으로의 위치 확인
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 주어진 범위를 벗어나는 경우 무시
                continue

            if graph[nx][ny] == 0: # 벽인 경우 무시
                continue

            if graph[nx][ny] == 1: # 해당 노드를 처음 방문하는 경우에 최단 거리 기록
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1] # 가장 오른쪽 아래까지의 최단 거리 반환

print(bfs(0, 0)) # 처음 위치 (1, 1)에서의 bfs 수행 결과 출력
