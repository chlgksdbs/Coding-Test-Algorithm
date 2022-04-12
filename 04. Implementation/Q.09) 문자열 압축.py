def solution(s):
    answer = 0
    
    d_list = [] # len(s)의 약수를 저장하는 리스트
    for i in range(1, len(s) + 1): # 1부터 len(s)까지의 약수 구하기
        if len(s) % i == 0:
            d_list.append(i)
    
    min = 1001 # 압축한 문자열의 길이 중 가장 짧은 길이를 저장하는 변수
    if len(s) == 1: # s의 길이가 1이면 "for x in range(1, len(s))"가 실행되지 않기때문에 예외처리를 해줌
        return len(s)
    else:
        for x in range(1, len(s)): # 1 단위부터 len(s) 크기의 단위로 문자열을 슬라이싱
            new_s = "" # 새롭게 만들어질 문자열
            i = 1
            s_slice = s[0:x]
            cnt = 1 # 같은 문자열이 몇 번 반복되는지
        
            while True:
                if i * x > len(s): # 입력된 문자열의 인덱스를 벗어나면 남은 문자열을 덧붙히고 반복문 탈출
                    if x not in d_list:
                        new_s += s[(i - 1) * x : len(s) + 1]
                    break
            
                if s_slice == s[i * x : (i + 1) * x]: # 같은 문자열이라면,
                    cnt += 1
                    i += 1
                else: # 서로 다른 문자열이라면,
                    if cnt == 1: # 반복 횟수가 1일 때는 해당 문자열만 추가
                        new_s += s_slice
                        s_slice = s[i * x : (i + 1) * x] # 변수 교체
                        i += 1
                    else: # 반복 횟수가 2이상일 때는 반복 횟수 + 문자열을 추가
                        new_s += str(cnt) + s_slice
                        s_slice = s[i * x : (i + 1) * x] # 변수 교체
                        i += 1
                        cnt = 1
                    
            if min > len(new_s): # 가장 짧은 길이 저장
                min = len(new_s)
    
    answer = min
    
    return answer
