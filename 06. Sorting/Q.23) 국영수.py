n = int(input()) # n : 학생의 수
student = [] # 학생의 정보를 담을 리스트

for i in range(n):
    data = input().split()
    student.append((data[0], int(data[1]), int(data[2]), int(data[3]))) # 학생의 이름, 국어, 영어, 수학 점수

student.sort(key=lambda x : (-x[1], x[2], -x[3], x[0])) # 국어 점수 내림차순, 영어 점수 오름차순, 수학 점수 내림차순, 이름 오름차순

for i in range(n): # 정렬된 리스트의 학생의 이름을 출력
    print(student[i][0])
