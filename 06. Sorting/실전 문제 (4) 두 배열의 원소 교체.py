n, k = map(int, input().split()) # n : 배열 A, B의 크기, k : 최대 바꿔치기 연산 횟수
arr = list(map(int, input().split())) # 배열 A
brr = list(map(int, input().split())) # 배열 B

arr.sort() # 오름차순 정렬
brr.sort(reverse=True) # 내림차순 정렬

for i in range(k):
    if arr[i] < brr[i]: # brr의 i번째 원소가 arr의 i번째 원소보다 큰 경우
        arr[i], brr[i] = brr[i], arr[i] # 스와프
    else: # 위의 경우에 해당하지 않는 경우 반복문 탈출
        break

print(sum(arr))

# 두 배열의 원소가 최대 100,000개까지 입력될 수 있으므로 O(NlogN)을 보장하는 정렬 알고리즘을 이용해야 한다.
# 변수명.sort() : 기본 정렬 기능으로 오름차순으로 정렬한다. (시간복잡도 : O(NlogN))
# 변수명.sort(reverse = True) : 기본 정렬 기능으로 내림차순으로 정렬한다. (시간복잡도 : O(NlogN))
