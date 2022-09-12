t = int(input()) # t : 테스트 케이스의 수
for _ in range(t):
    # n : 세로의 크기, m : 가로의 크기
    n, m = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    temp = list(map(int, input().split())) # n x m개의 위치에 매장된 금의 개수를 공백으로 구분하여 입력
    temp_idx = 0

    # 1차원 리스트로 입력한 데이터를 2차원 리스트로 옮기는 작업
    for i in range(n):
        for j in range(m):
            graph[i][j] = temp[temp_idx]
            temp_idx += 1

    d = [[0] * m for _ in range(n)] # 2차원 dp 테이블 생성
    for i in range(n):
        d[i][0] = graph[i][0] # graph 리스트의 첫 번째 열 데이터를 dp 테이블 첫 번째 열에 삽입
    
    for j in range(1, m):
        for i in range(n): # 1열씩 체크
            if i == 0:
                d[i][j] = graph[i][j] + max(d[i][j - 1], d[i + 1][j - 1]) # 첫 번째 행인 경우 (1) 오른쪽으로 이동, (2) 오른쪽 아래로 이동의 2가지 경우의 수가 존재
            elif i == (n - 1):
                d[i][j] = graph[i][j] + max(d[i][j - 1], d[i - 1][j - 1]) # 마지막 행인 경우 (1) 오른쪽으로 이동, (2) 오른쪽 위로 이동의 2가지 경우의 수가 존재
            else:
                d[i][j] = graph[i][j] + max(d[i][j - 1], d[i - 1][j - 1], d[i + 1][j - 1]) # (1) 오른쪽으로 이동, (2) 오른쪽 위로 이동, (3) 오른쪽 아래로 이동의 3가지 경우의 수가 존재
    
    result = 0
    for i in range(n):
        if result < d[i][m - 1]: # 최댓값 저장
            result = d[i][m - 1]
    
    print(result)