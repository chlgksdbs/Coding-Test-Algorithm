n = int(input()) # 동전의 개수 입력
min_value = 1 # 주어진 동전들로 만들 수 없는 최솟값
data = list(map(int, input().split())) # 각 동전의 화폐 단위 입력
data.sort() # 오름차순 정렬

while True:
    result = min_value
    for i in range(len(data) - 1, -1, -1): # 큰 수부터 result와 빼기 연산
        if result - data[i] >= 0:
            result -= data[i]
    if result == 0:
        min_value += 1
    else:
        break

print(min_value) # 결과 값 출력

# 답지를 봤을 때, for문을 리스트 요소에 직접 접근하여 풀이를 진행하였다.
# Python 문법은 for문의 인덱스 접근이 아닌 리스트에 요소로 직접 접근이 가능한데, 이 문법에 대해 공부를 해봐야겠다는 생각을 했다.

''' A04.py 답안 예시

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x
    
# 만들 수 없는 금액 출력
print(target)

'''
