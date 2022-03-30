data = list(map(int, input())) # 0과 1로만 이루어진 문자열 S 입력
count_0 = 0 # 연속된 숫자 0을 count 하는 변수
count_1 = 0 # 연속된 숫자 1을 count 하는 변수
i = 0 # while 반복문에서 사용될 변수

while i < len(data):
    num = data[i]
    if i < (len(data) - 1) and num == data[i + 1]: # data의 다음 수가 num과 같다면,
        i += 1
    else: # data의 다음 수가 num과 다르다면,
        if num == 0:
            count_0 += 1
        else:
            count_1 += 1
        i += 1

if count_0 < count_1: # 0을 counting한 변수보다 1을 counting한 변수가 더 크다면,
    print(count_0)
else: # 위의 경우가 아니라면,
    print(count_1)
