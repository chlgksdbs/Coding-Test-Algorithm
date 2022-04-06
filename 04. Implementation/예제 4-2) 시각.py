import time
start_time = time.time()

n = int(input())
count = 0 # 3을 포함하는 시각의 개수를 count하는 변수
st_time = 1 
ed_time = 3600 * (n + 1) # 1시간은 60분이고, 1분은 60초이므로 1시간은 3600초이다.

for i in range(st_time, ed_time): # 00:00:01 ~ n:59:59
    a = i // 3600 # a는 hour(시간)
    b = (i % 3600) // 60 # b는 min(분)
    c = (i % 3600) % 60 # c는 sec(초)

    if c // 10 == 3 or c % 10 == 3: # 0 <= c <= 59 이므로, c는 10의 자리와 1의 자리 모두 3이 있는지 체크
        count += 1
    elif b // 10 == 3 or b % 10 == 3: # 0 <= b <= 59 이므로, b는 10의 자리와 1의 자리 모두 3이 있는지 체크
        count += 1
    elif a % 10 == 3: # 0 <= a <= 23 이므로, a는 10의 자리가 3이 나올 수 없음. 따라서 1의 자리만 체크
        count += 1

print(count)

# n = 5를 입력했을 때, 1.1012985706329346 시간경과


# 4-2.py 답안 예시

'''
n = int(input())

count = 0
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)
'''

# n = 5를 입력했을 때, 1.5657799243927002 시간경과

end_time = time.time()
print(end_time - start_time)
