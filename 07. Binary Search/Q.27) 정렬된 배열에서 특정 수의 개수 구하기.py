import bisect

def x_count(data, target): # data 리스트에서 target 원소의 개수 구하는 함수
    left_index = bisect.bisect_left(data, target)
    right_index = bisect.bisect_right(data, target)
    return (right_index - left_index)


n, x = map(int, input().split()) # n : 수열의 크기, x : 찾아야 할 원소
data = list(map(int, input().split()))

if x_count(data, x) == 0:
    print(-1)
else:
    print(x_count(data, x))