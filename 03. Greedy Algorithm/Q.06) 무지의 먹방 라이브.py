def solution(food_times, k):
    answer = 0
    
    if k < len(food_times): # 만약 k의 값이 배열의 길이보다 작다면,
        answer = k + 1
        
    else:
        lens = len(food_times)
        while True:
            k -= lens
            for i in range(len(food_times)):
                food_times[i] -= 1 # 모든 원소를 1만큼 뺀다 (1 cycle)
            cnt = food_times.count(0) # 0이 추가된 횟수
            if k < (lens - cnt):
                break
            else:
                lens -= cnt
        
        if max(food_times) <= 0:
            return -1
        else:       
            i = 0
            while k >= 0:
                    if food_times[i] > 0:
                        answer += 1
                        i += 1
                        k -= 1
                    else:
                        answer += 1
                        i += 1
                    if k < 0:
                        break
                        
    return answer
  
# 위 문제는 2019 KAKAO BLIND RECRUITMENT 문제로, 무지의 먹방 라이브라는 제목의 문제이다.
# 프로그래머스로 채점 결과, 정확성 테스트에선 28 / 32의 정답률이 나왔고, 효율성 테스트에선 0 / 8의 정답률이 나왔다.
# 채점 결과 점수 : 37.5 / 100.0
