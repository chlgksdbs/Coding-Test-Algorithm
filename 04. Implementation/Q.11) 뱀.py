n = int(input()) # n : 보드의 크기
k = int(input()) # k : 사과의 개수
loc_apple = [] # 사과의 위치

for i in range(k):
    x = list(map(int, input().split())) # 첫 번째 정수 : 행 위치, 두 번째 정수 : 열 위치
    loc_apple.append(x)

l = int(input()) # l : 뱀의 방향 변환 횟수
info_snake = [] # 뱀의 방향 변환 정보

for i in range(l):
    y = list(input().split()) # 정수 + 문자
    info_snake.append(y)

# ---------- 입력 끝, 구현 시작

result = 0 # 게임이 끝나는 시간
loc_snake = [[1, 1]] # 뱀의 현재 위치 정보
move_index = 0 # 현재 움직임 (default : 오른쪽)
l_index = 0 # 뱀의 방향 변환 정보 리스트의 인덱스를 표현
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while True:
    for i in range(4): # step 1) 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다
        if i == move_index:
            nx = loc_snake[0][0] + dx[i]
            ny = loc_snake[0][1] + dy[i]
    
    result += 1 # 이동 후, 시간 증가
    if nx < 1 or nx > n or ny < 1 or ny > n or [nx, ny] in loc_snake: # 정사각 보드 범위를 벗어났거나, 뱀이 자기자신의 몸과 부딪힌다면,
        break
    
    if [nx, ny] in loc_apple: # step 2) 뱀이 이동한 칸에 사과가 있다면, 그 칸에 있던 사과는 없어지고 꼬리는 움직이지 않는다
        loc_apple.remove([nx, ny])
        loc_snake.append([loc_snake[0][0], loc_snake[0][1]]) # 꼬리 좌표 추가
    
    for j in range(len(loc_snake) - 1, 0, -1): # 뱀의 몸 좌표도 변경 (역순으로 해야 값을 옮기기 수월함)
        loc_snake[j][0] = loc_snake[j - 1][0]
        loc_snake[j][1] = loc_snake[j - 1][1]        
    
    loc_snake[0][0] = nx
    loc_snake[0][1] = ny
    
    if l_index < len(info_snake) and int(info_snake[l_index][0]) == result: # 방향 전환
        if info_snake[l_index][1] == 'D': # 오른쪽
            move_index += 1
            l_index += 1
        else: # 왼쪽
            move_index -= 1
            l_index += 1
    
    move_index %= 4 # move_index를 0, 1, 2, 3의 값으로 변경

print(result) # 결과 출력
