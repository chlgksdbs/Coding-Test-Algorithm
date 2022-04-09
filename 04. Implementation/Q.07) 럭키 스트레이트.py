n = input()
left_sum = 0
right_sum = 0

for i in range(len(n)):
    if i < (len(n) // 2): # 왼쪽 부분
        left_sum += int(n[i])
    else: # 오른쪽 부분
        right_sum += int(n[i])
    
if left_sum == right_sum: # 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합이 같다면
    print("LUCKY")
else: # 합이 다르다면
    print("READY")
