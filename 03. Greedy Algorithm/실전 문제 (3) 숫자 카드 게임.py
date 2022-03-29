# 1. min() 함수를 이용하는 답안 예시

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)
    
print(result) # 최종 답안 출력



# 2. 2중 반복문 구조를 이용하는 답안 예시

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001 # 입력 조건에서 입력으로 들어오는 수는 모두 10,000 이하이므로 해당 변수를 설정
    for a in data:
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)
    
print(result) # 최종 답안 출력



# 3. 필자 답안

n, m = map(int, input().split()) # n : 행의 개수, m : 열의 개수
arr = [] # n x m개의 리스트를 담을 공간
arr_min = [] # arr의 각 행에서 가장 작은 수를 담는 리스트

for i in range(n): # 행의 개수만큼 반복
    x = list(map(int, input().split())) # 열의 개수만큼 입력
    arr.append(x)
    arr_min.append(min(x)) # 각 행의 최솟값을 arr_min 리스트에 추가

print(max(arr_min)) # arr_min 중, 가장 큰 값을 출력

# 필자의 코드는 리스트를 활용한 코드이다. 반복문에서 받은 입력 값을 초기에 선언한 리스트인 arr에 추가함으로써, 2중 리스트를 이용하여 문제를 해결하였다.
