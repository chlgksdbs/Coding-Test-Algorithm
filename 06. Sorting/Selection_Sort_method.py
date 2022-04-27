# 선택 정렬(Selection Sort)
# 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복하는 정렬

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr) - 1):
    min_idx = i # 가장 작은 원소의 인덱스를 담을 변수
    for j in range(i + 1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j
    
    arr[min_idx], arr[i] = arr[i], arr[min_idx] # 스와프

print(arr)
