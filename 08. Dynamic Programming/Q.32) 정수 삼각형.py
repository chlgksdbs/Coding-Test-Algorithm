n = int(input()) # n : 삼각형의 크기
intTriangle = [] # intTriangle : 정수 삼각형의 값을 담는 리스트
for _ in range(n):
    # intValue : 삼각형을 이루는 각 층의 값을 입력
    intValue = list(map(int, input().split()))
    intTriangle.append(intValue)

for i in range(1, n):
    # 이전 층에서 더할 수 있는 값 중, 큰 값을 더하여 합의 최댓값을 저장
    for j in range(len(intTriangle[i])):
        if j == 0: # 맨 왼쪽 항의 경우, 경우의 수는 1가지
            intTriangle[i][j] += intTriangle[i - 1][j]
        elif j == len(intTriangle[i]) - 1: # 맨 오른쪽 항의 경우에도, 경우의 수는 1가지
            intTriangle[i][j] += intTriangle[i - 1][j - 1]
        else: # 위 두 항의 경우를 제외하고, 왼쪽 대각선과 오른쪽 대각선의 값 중, 큰 값을 더하여 리스트 갱신
            intTriangle[i][j] += max(intTriangle[i - 1][j], intTriangle[i - 1][j - 1])

print(max(intTriangle[n - 1])) # 합이 최대가 되는 경로에 있는 수의 합 출력