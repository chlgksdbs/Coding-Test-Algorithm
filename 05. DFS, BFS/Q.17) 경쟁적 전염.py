from collections import deque

# (1) 데이터 입력
n, k = map(int, input().split()) # n : 시험관의 크기, k : 바이러스 종류의 개수
graph = []
for _ in range(n): # 시험관의 정보 입력
    graph.append(list(map(int, input().split())))
s, a, b = map(int, input().split()) # s : s초 후 시간, a, b : 결과를 출력할 좌표


# (2) 문제 수행
data = [] # 바이러스가 존재하는 칸의 정보(x좌표, y좌표, 바이러스의 종류)
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            data.append([i, j, graph[i][j]])

while s > 0: # s초동안 수행
    s -= 1
    data.sort(key = lambda data : data[2], reverse = True) # 바이러스 번호를 기준으로 정렬(낮은 번호부터 수행하는 문제 조건), queue에 data가 pop이 되는 형식으로 들어가기 때문에 내림차순으로 정렬

    # (3) bfs 부분 코드
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    for i in range(len(data)):
        q.append(data.pop()) # queue에 삽입되는 정보들은 차례대로 x, y, 바이러스의 종류 번호

    while q: # 현재 queue가 빌 때까지만, 즉 1초 동안의 시간동안 bfs 수행
        x, y, num = q.popleft()
        for i in range(4): # 상, 하, 좌, 우에 대해 수행
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n: # 범위를 벗어날 경우
                continue

            if graph[nx][ny] == 0: # 해당 노드가 빈칸일 경우
                graph[nx][ny] = num # 해당 바이러스의 종류로 감염
                data.append([nx, ny, num]) # 추가된 영역을 data 리스트에 저장

# (4) 데이터 출력
print(graph[a - 1][b - 1]) # s초 뒤에 (X,Y)에 존재하는 바이러스의 종류 출력


# 문제 채점 결과로 시간 초과 발생 시, 반복 횟수를 줄일 수 있는 경우를 체크하자!
