n = int(input()) # n : 집의 수
data = list(map(int, input().split())) # n채의 집의 위치를 담을 리스트

data.sort() # 오름차순 정렬
print(data[(n - 1) // 2]) # 정렬 된 집의 위치 값 중, 가운데 값에 안테나를 설치하면 모든 집까지의 거리의 총 합이 최소가 된다.
