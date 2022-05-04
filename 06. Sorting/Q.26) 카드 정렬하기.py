import heapq

n = int(input()) # 숫자 카드 묶음의 크기인 n 입력
data = []

for _ in range(n):
    data.append(int(input())) # 숫자 카드 묶음의 각각의 크기 입력

heapq.heapify(data) # data 리스트를 최소 heap 으로 변환
result = 0 # 계산 결과를 누적하여 저장할 변수 (최소 비교 횟수를 저장할 변수)

while True:
    if len(data) < 2: # 리스트의 원소가 두개보다 작을 때 반복문 종료 
        break
    
    # 리스트에서 가장 작은 원소와 그 다음 작은 원소 추출
    a = heapq.heappop(data)
    b = heapq.heappop(data)
    
    ab_sum = a + b # 두 원소의 합 계산
    heapq.heappush(data, ab_sum) # 위의 계산 값을 최소 heap에 푸쉬
    result += ab_sum # 위의 계산 값을 result에 더하여 저장

print(result) # 최소 비교 횟수 출력
