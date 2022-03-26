# 1. 단순하게 푸는 답안 예시

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

result = 0

while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
        if m == 0: # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 # 더할 때마다 1씩 빼기
    if m == 0: # m이 0이라면 반복문 탈출
        break
    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1 # 더할 때마다 1씩 빼기
    
print(result)



# 2. 빠르게 동작하도록 푸는 답안 예시

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result)



# 3. 필자 답안

n, m, k = map(int, input().split()) # n : 배열의 크기, m : 덧셈의 양, k : 연속횟수
data = list(map(int, input().split())) # 크기가 n인 배열 입력
data.sort()
count = 0 # k만큼 연속하기 위해 counting하는 변수
sum = 0 # 계산 값을 저장하기 위한 변수

for i in range(m):
    if count == k:
        sum += data[n - 2] # 두 번째로 큰 값을 더함
        count = 0 # 다시 count 횟수 초기화
    else:
        sum += data[n - 1] # 가장 큰 값을 더함
        count += 1

print(sum)
