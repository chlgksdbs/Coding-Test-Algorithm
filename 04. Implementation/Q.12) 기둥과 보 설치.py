def check_build(data): # 삭제, 설치 이후 현재 설치된 구조물이 가능한 구조물인지 체크하는 함수
    for x, y, stuff in data:
        if stuff == 0: # 1) 기둥의 경우
            # 바닥 위, 보의 한쪽 끝 부분, 다른 기둥 위라면 가능
            if y == 0 or [x - 1, y, 1] in data or [x, y, 1] in data or [x, y - 1, 0] in data:
                continue
            return False # 아니라면 거짓을 반환
        elif stuff == 1: # 2) 보의 경우
            # 한쪽 끝 부분이 기둥 위, 양쪽 끝 부분이 다른 보와 동시에 연결이라면 가능
            if [x, y - 1, 0] in data or [x + 1, y - 1, 0] in data or ([x - 1, y, 1] in data and [x + 1, y, 1] in data):
                continue
            return False # 아니라면 거짓을 반환
    return True
            


def solution(n, build_frame):
    answer = []
    
    for frame in build_frame: # 작업의 개수는 max 1000개
        x, y, stuff, operate = frame
        if operate == 0: # 1) 삭제
            answer.remove([x, y, stuff]) # 일단 삭제 해본 뒤에
            if not check_build(answer): # 가능한지 체크
                answer.append([x, y, stuff]) # 가능하지 않다면 다시 설치
        
        if operate == 1: # 2) 설치
            answer.append([x, y, stuff]) # 일단 설치 해본 뒤에
            if not check_build(answer): # 가능한지 체크
                answer.remove([x, y, stuff]) # 가능하지 않다면 다시 삭제
    
    return sorted(answer) # 정렬된 결과를 반환
