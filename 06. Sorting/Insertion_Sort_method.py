# 삽입 정렬(Insertion Sort)
# 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입 하는 정렬

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하며 반복하는 문법
        if arr[j] < arr[j - 1]: # 한 칸씩 왼쪽으로 이동
            arr[j], arr[j - 1] = arr[j - 1], arr[j] # 스와프
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 반복문 탈출
            break

print(arr)
