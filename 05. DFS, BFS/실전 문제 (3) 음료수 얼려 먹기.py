def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m: # 크기를 벗어날 때,
        return False
    if graph[x][y] == 0: # 구멍이 뚫려 있는 부분인 경우
        graph[x][y] = 1 # 구멍이 뚫려 있는 현재 위치를 1로 변경
        dfs(x - 1, y) # 상
        dfs(x + 1, y) # 하
        dfs(x, y - 1) # 좌
        dfs(x, y + 1) # 우
        # 현재의 노드에서 연결되어있는 상하좌우 모두 재귀함수를 이용하여 1값으로 변경
        return True
    return False

n, m = map(int, input().split()) # n, m 입력
graph = [] # n X m 크기를 위한 리스트
for i in range(n):
    graph.append(list(map(int, input()))) # 띄어쓰기 없이 m만큼의 크기 입력

result = 0 # 아이스크림의 개수를 counting하는 변수
for i in range(n): # n행 반복
    for j in range(m): # m열 반복
        if dfs(i, j) == True:
            result += 1

print(result)
