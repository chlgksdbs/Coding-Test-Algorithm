n = int(input()) # 모험가의 수 N 입력
max_count = 0 # 그룹 수의 최댓값
horror_degree = 0 # 공포도
data = list(map(int, input().split())) # 각 모험가의 공포도 입력
data.sort() # 오름차순으로 정렬

i = 0 # while 반복문에서 인덱스 접근을 위해 사용될 변수
while i < n:
    horror_degree = data[i]
    j = data[i] # 두번째 while 반복문에서 그룹 count를 위해 사용될 변수
    while j > 1:
        i += 1
        j -= 1
        if i < n and horror_degree != data[i]: # 리스트의 다음 원소가 이전 원소와 공포도가 다르다면,
            j += data[i] - horror_degree # j값을 증가
            horror_degree = data[i] # horror_degree값을 변경
    if i < n:
        i += 1
        max_count += 1
    else:
        break

print(max_count) # 출력

# 이 문제에 답안을 보면, 반복문이 하나만 사용되어 시간복잡도가 O(N)이지만, 필자의 답안을 보면 이중 반복문이 사용되어 시간복잡도가 이보다 증가할 것 같다.
# 그리디 문제를 해결할 때 항상 최적의 방법으로 문제를 해결하는 방법을 생각해봐야 할 것 같다.
