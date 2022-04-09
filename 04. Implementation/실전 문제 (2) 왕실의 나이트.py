x = input()
x_column = x[0] # 열을 나타내는 부분, 즉 범위는 ('a' ~ 'h')
x_row = x[1] # 행을 나타내는 부분, 즉 범위는 (1 ~ 8)
count = 0 # 경우의 수를 세는 변수

if 'c' <= x[0] and x[0] <= 'f': # (1) 수평으로 두 칸 이동하는 경우의 수
    if '2' <= x[1] and x[1] <= '7': # 수직으로 한 칸 이동하기
        count += 4
    else:
        count += 2
else:
    if '2' <= x[1] and x[1] <= '7':
        count += 2
    else:
        count += 1

if '3' <= x[1] and x[1] <= '6': # (2) 수직으로 두 칸 이동하는 경우의 수
    if 'b' <= x[0] and x[0] <= 'g': # 수직으로 한 칸 이동하기
        count += 4
    else:
        count += 2
else:
    if 'b' <= x[0] and x[0] <= 'g':
        count += 2
    else:
        count += 1

print(count)


# 4-3.py 답안 예시

'''
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result +=1

print(result)
'''

# 나이트의 8가지 경로를 하나씩 확인하며 각 위치로 이동이 가능한지 확인한다.
# 리스트를 이용하여 8가지 방향에 대한 방향 벡터를 정의한다.
