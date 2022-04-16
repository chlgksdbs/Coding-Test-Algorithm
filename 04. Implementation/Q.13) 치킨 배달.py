from itertools import combinations # 조합

n, m = map(int, input().split()) # n : 도시의 크기, m : 폐업시키지 않을 치킨집의 개수
data = []

for i in range(n):
    data.append(list(map(int, input().split()))) # n X n 크기의 도시의 정보 입력

loc_home = [] # 집의 위치 정보를 담을 리스트
loc_chicken = [] # 치킨집의 위치 정보를 담을 리스트

for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            loc_home.append([i, j]) # 집의 위치 정보 수집
        elif data[i][j] == 2:
            loc_chicken.append([i, j]) # 치킨집의 위치 정보 수집

comb_chicken = list(combinations(loc_chicken, m)) # 모든 치킨집의 경우에서 m만큼 combination 적용
result = [] # 각 치킨집의 경우에 따른 치킨 거리의 최솟값을 담을 리스트

for i in range(len(comb_chicken)):
    min_sum = 0 # 각 조합의 경우의 수마다 도시의 치킨 거리의 최솟값을 저장하는 변수
    for j in range(len(loc_home)):
        min = 2500 # 치킨 거리의 최솟값을 담을 변수, n의 최대 크기가 50이므로 2500의 크기로 초기화
        for k in range(len(comb_chicken[i])):
            length = abs(loc_home[j][0] - comb_chicken[i][k][0]) + abs(loc_home[j][1] - comb_chicken[i][k][1]) # 각 집마다 모든 치킨집과의 거리 계산
            if min > length: # 각 집마다의 모든 치킨집과의 거리 중 최솟값을 저장
                min = length
        min_sum += min
    result.append(min_sum)

result.sort()
print(result[0]) # 구한 경우의 수 중, 최솟값을 출력
