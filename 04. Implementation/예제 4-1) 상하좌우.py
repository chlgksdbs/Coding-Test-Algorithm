n = int(input()) # 공간의 크기 N 입력
move_dist = list(input().split()) # 여행가 A가 이동할 계획서 내용 입력
x, y = 1, 1 # 시작 위치

for d in move_dist:
    if d == 'R' and y < n:
        y += 1
    elif d == 'L' and 1 < y:
        y -= 1
    elif d == 'U' and 1 < x:
        x -= 1
    elif d == 'D' and x < n:
        x += 1

print(x, y)

# 필자는 이 문제에 대한 접근방법을 직관적으로 입력받은 문자에 대해 체크하고, 공간을 벗어나는 경우또한 체크한 뒤 x, y 값을 조정하여 문제를 해결하였다.
# 그러나 책의 답안에서는 x, y에 대한 이동방향을 배열로 저장하고, 문자 타입또한 배열로 저장하여 효과적으로 문제를 해결하였다.
# 이러한 2차원 공간적인 문제는 행렬, 즉 방향 벡터와 같이 배열을 사용하여 문제를 해결할 수 있도록 노력해야겠다.
# 또한 이러한 문제를 풀 때, 이동방향에 따른 증, 감소량이 x, y값에 대응하는지 잘 체크해야겠다.


# 4-1.py 답안 예시

# N을 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)
