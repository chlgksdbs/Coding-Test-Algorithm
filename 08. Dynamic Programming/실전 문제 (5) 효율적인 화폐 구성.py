# n : 화폐 종류의 개수, m : 만들어야 하는 가치의 합
n, m = map(int, input().split())
array = []
for i in range(n): # 입력
    temp = int(input())
    array.append(temp)

d = [10001] * (m + 1) # 계산된 결과를 저장하기 위한 DP 테이블 초기화, 만들 수 없다는 의미로 10001로 초기화
d[0] = 0 # 0원을 만들기 위한 최소한의 화폐 개수는 0개

for i in range(n): # i는 각각의 화폐 단위를 의미
    for j in range(array[i], m + 1): # j는 각각의 금액을 의미
        if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001: # m원을 만드는 것이 불가능한 경우
    print(-1)
else:
    print(d[m])