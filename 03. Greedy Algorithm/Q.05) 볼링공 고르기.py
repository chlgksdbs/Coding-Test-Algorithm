n, m = map(int, input().split()) # N : 볼링공의 개수, M : 볼링공의 무게 (1 ~ M)
data = list(map(int, input().split())) # N개 만큼 입력
count = 0 # 경우의 수

for i in range(0, n - 1): # A가 고르는 볼링공
    for j in range(i + 1, n): # B가 고르는 볼링공
        if data[i] != data[j]:
            count += 1

print(count)

# 필자는 이 문제를 직관적으로 풀이하여 모든 경우의 수를 다 고려했다.
# 그 결과, 이중 for문을 사용했고, 시간복잡도가 높게 나왔다.
# 답안지의 풀이의 경우, 문제를 효과적으로 해결하기 위해 무게마다 볼링공의 개수를 카운트하였고, 경우의 수에따라 풀이를 하였다
# 그 결과, for문을 하나만 사용했고, 시간복잡도가 상대적으로 낮게 나왔다.

''' A05.py 답안 예시
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11 # array 배열을 생성하여 크기 11만큼을 0으로 초기화

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1
    
result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기
    
print(result)
'''

# A04와 A05 문제의 답안에서 확인해보면, Python에서의 for문 문법 중, 인덱스 접근이 아닌 리스트 요소에 직접 접근하는 문법을 사용하고 있다.
# 이와 같은 문법을 사용하면, Python의 장점을 살려 문제를 더욱 쉽게 해결할 수 있을 것 같다는 생각이 들었다.
