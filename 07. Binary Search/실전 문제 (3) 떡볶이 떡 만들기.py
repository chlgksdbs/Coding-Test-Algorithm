import sys
import copy

# n : 떡의 개수, m : 손님이 요청한 떡의 길이
n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split())) # 떡의 개별 높이 입력

# 이진 탐색 시에 활용될 시작점과 끝점, 여기서는 인덱스 활용이 아닌 리스트의 최대 값과 최소 값이 될 수 있는 0을 활용
start = 0
end = max(data)
# 이진 탐색 종료 시에 반환될 값
target = -1

while start <= end:
    temp = copy.deepcopy(data) # data 리스트를 temp 리스트에 깊은 복사
    # 중간값 설정
    mid = (start + end) // 2

    for i in range(len(temp)):
        if temp[i] > mid: # x가 mid보다 크다면 mid와 빼기 연산
            temp[i] -= mid
        else: # x가 mid보다 작거나 같다면 0으로 만듦
            temp[i] = 0
    
    temp_sum = sum(temp) # 위 연산을 통해 나온 temp 리스트의 값들의 합을 계산

    if temp_sum == m: # 잘린 떡의 길이의 합이 손님이 요청한 떡의 길이와 같다면 그 값을 target에 저장하고 반복문 탈출
        target = mid
        break
    elif temp_sum > m: # 잘린 떡의 길이의 합이 손님이 요청한 떡의 길이보다 크다면 오른쪽 탐색
        start = mid + 1
    else: # 잘린 떡의 길이의 합이 손님이 요청한 떡의 길이보다 작다면 왼쪽 탐색
        end = mid - 1

if target == -1: # 이진 탐색을 통해 손님이 요청한 떡의 길이가 정확하게 도출되지 않았다면 그에 근접한 mid 값에 1을 빼서 출력
    print(mid - 1)
else: # 이진 탐색을 통해 손님이 요청한 떡의 길이가 정확하게 도출되었다면 그 값을 출력
    print(target)
