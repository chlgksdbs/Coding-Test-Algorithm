def binary_search(arr, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == mid: # arr[mid] 값과 mid값이 같다면 mid값을 반환
            return mid
        elif arr[mid] > mid: # arr[mid] 보다 mid값이 작다면 왼쪽을 탐색
            end = mid - 1
        else: # arr[mid] 보다 mid값이 크다면 오른쪽을 탐색
            start = mid + 1
        
    return 0

n = int(input()) # n : 수열의 크기
data = list(map(int, input().split()))
result = binary_search(data, 0, n - 1)

if result: # binary_search 함수의 반환 값이 존재한다면 그 값을 출력
    print(result)
else: # binary_search 함수의 반환 값이 존재하지 않는다면 -1을 출력
    print(-1)