# 피보나치 함수(Fibonacci Function)를 재귀 함수로 구현
def fibo(x):
    if x == 1 or x == 2: # 첫 번째와 두 번째 피보나치 수는 1, 재귀 함수의 종료 조건
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4)) # 실행결과 : 3
print(fibo(6)) # 실행결과 : 8
print(fibo(11)) # 실행결과 : 89

# 단순 재귀 함수로 피보나치 수열을 해결하면 지수 시간 복잡도를 가진다.