n = int(input())
data = [] # n개의 수를 저장할 리스트

for i in range(n):
    data.append(int(input()))

data.sort(reverse = True) # 내림차순 정렬

for i in range(n):
    print(data[i], end = ' ')
