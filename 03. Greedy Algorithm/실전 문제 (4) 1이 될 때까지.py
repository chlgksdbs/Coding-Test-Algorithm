# 1. 단순하게 푸는 답안 예시

n, k = map(int, input().split())
count = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        count += 1
    # K로 나누기
    n //= k
    count += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    count += 1

print(count)



# 2. 빠르게 동작하도록 푸는 답안 예시

# N, K를 공백으로 구분하여 입력받기
n, k = map(int, input().split())
count = 0

while True:
    # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    count += (n - target)
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    count += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
count += (n - 1)
print(count)
# 위 코드는 33 ~ 35번째 line이 핵심이라고 할 수 있다. 1번 풀이와 다르게 반복문 1개를 통해 수행하기 때문에 시간을 효율적으로 줄일 수 있다.



# 3. 필자 답안

n, k = map(int, input().split())
count = 0

while n > 1:
    if n % k == 0:
        n /= k
        count += 1
    else:
        n -= 1
        count += 1

print(count)

# 위 코드는 N값에 대해서 하나씩 수행하는 것으로 비효율적인 코드라고 생각이 든다.
