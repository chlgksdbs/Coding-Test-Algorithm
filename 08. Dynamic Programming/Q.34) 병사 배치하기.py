n = int(input()) # n : 병사의 수
array = list(map(int, input().split())) # 각 병사의 전투력을 담는 리스트
array.reverse() # 리스트의 순서를 뒤집어 '가장 긴 증가하는 부분 수열' 문제로 변환

d = [1] * n # dp 테이블

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            d[i] = max(d[i], d[j] + 1)

print(n - max(d)) # 열외시켜야 하는 병사의 최소 수를 출력