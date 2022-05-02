def solution(N, stages):
    answer = []
    stage_fail = [] # 각 스테이지 별 실패율을 담을 리스트
    all_count = len(stages) # 현 스테이지의 총 도전자 수
    
    for i in range(1, N + 1):
        stage_count = stages.count(i) # 현 스테이지를 클리어하지 못한 사용자 수
        
        if stage_count == 0: # 해당 스테이지에 도달한 유저가 없는 경우
            stage_fail.append([0, i])
        else: # 해당 스테이지에 도달한 유저가 있는 경우
            stage_fail.append([stage_count / all_count, i]) # 현 스테이지의 실패율과 인덱스 번호를 저장
            all_count -= stage_count # 다음 스테이지는 현 스테이지를 클리어하지 못한 사용자 수가 제외됨
    
    stage_fail.sort(key = lambda x : (-x[0])) # 실패율을 기준으로 내림차순 정렬, 실패율이 같은 경우 낮은 숫자부터 정렬
    
    for i in range(N):
        answer.append(stage_fail[i][1]) # 정렬된 스테이지의 번호를 answer 리스트에 차례대로 추가
        
    return answer
