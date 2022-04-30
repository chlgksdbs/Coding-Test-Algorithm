n = int(input()) # 학생의 수 입력

data = [] # 학생의 이름, 학생의 성적
for i in range(n):
    input_data = input().split()
    data.append((input_data[0], int(input_data[1]))) # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장

new_data = sorted(data, key=lambda x : x[1]) # key를 이용하여 점수를 기준으로 오름차순 정렬
for i in range(n):
    print(new_data[i][0], end=' ')
