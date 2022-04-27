# 퀵 정렬(Quick Sort)
# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 정렬

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def QuickSort(arr, start, end):
    if start >= end: # 리스트의 원소가 1개인 경우 함수 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    i = start + 1 # left
    j = end # right

    while i <= j:
        while i <= end and arr[i] <= arr[pivot]: # 피벗보다 큰 데이터를 찾을 때까지 반복
            i += 1
        while j > start and arr[j] >= arr[pivot]: # 피벗보다 작은 데이터를 찾을 때까지 반복
            j -= 1
        
        if i > j: # 엇갈렸을 때 작은 데이터와 피벗을 교체
            arr[pivot], arr[j] = arr[j], arr[pivot]
        else: # 엇갈리지 않았을 때 작은 데이터와 큰 데이터를 교체
            arr[i], arr[j] = arr[j], arr[i]
    
    # 분할 이후 j값(right값)을 기준으로 왼쪽 부분과 오른쪽 부분에 대해서 각각 퀵 정렬 수행
    QuickSort(arr, start, j - 1)
    QuickSort(arr, j + 1, end)

QuickSort(arr, 0, len(arr) - 1)
print(arr)

'''
* 파이썬의 장점을 살린 퀵 정렬 소스코드

arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def QuickSort(arr):
    if len(arr) <= 1: # 리스트가 하나 이하의 원소만을 담고 있다면 함수 종료
        return arr
    
    pivot = arr[0] # 피벗은 리스트의 첫 번째 원소
    tail = arr[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에 대해서 각각 퀵 정렬을 수행하고, 전체 리스트를 반환
    return QuickSort(left_side) + [pivot] + QuickSort(right_side)

print(QuickSort(arr))
'''
