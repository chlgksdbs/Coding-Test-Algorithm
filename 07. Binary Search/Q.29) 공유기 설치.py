import sys

# n : 집의 개수, c : 공유기의 개수
n, c = map(int, input().split())
data = []
for i in range(n):
    temp = int(sys.stdin.readline())
    data.append(temp)
data.sort() # 이진 탐색을 위한 오름차순 정렬

start = 1 # 공유기 사이 거리의 최솟값(min gap)
end = data[-1] - data[0] # 공유기 사이 거리의 최댓값(max gap)
result = 0 # 가장 인접한 두 공유기 사이의 최대 거리를 저장하는 변수

while start <= end:
    mid = (start + end) // 2 # mid는 가장 인접한 두 공유기 사이의 거리(gap)을 의미
    count = 1 # 설치 가능한 공유기의 개수를 count하는 변수, data[0]은 항상 설치한다고 가정
    value = data[0]

    # 현재의 mid값을 이용해 공유기 설치
    for i in range(1, n): # 앞에서부터 차례대로 설치
        if data[i] >= value + mid:
            value = data[i]
            count += 1
    
    if count >= c: # c개 이상의 공유기를 설치할 수 있는 경우 거리 증가
        start = mid + 1
        result = mid
    else: # c개 이상의 공유기를 설치할 수 없는 경우 거리 감소
        end = mid -1

print(result)