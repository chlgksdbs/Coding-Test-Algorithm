# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100 # 여기서는 99번째 피보나치 수를 구할 목적이므로 99번째 index까지 생성

# 피보나치 함수(Fibonacci Function)를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
    if x == 1 or x == 2: # 종료조건
        return 1
    if d[x] != 0: # 이미 계산한 적 있는 문제라면 그대로 반환
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2) # 아직 계산한 적 없는 문제라면 점화식에 따라 피보나치 결과 반환
    return d[x]

print(fibo(99)) # 실행결과 : 218922995834555169026