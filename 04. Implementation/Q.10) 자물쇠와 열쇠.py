def rotate_matrix(data): # 시계방향으로 90도 회전
    row_len = len(data) # 행의 길이
    column_len = len(data[0]) # 열의 길이
    
    result = [[0] * row_len for _ in range(column_len)] # 회전 결과를 담을 리스트
    
    for i in range(row_len):
        for j in range(column_len):
            result[j][row_len - i - 1] = data[i][j]
    
    return result


def check(new_lock): # 자물쇠의 중간 부분이 모두 1인지 확인
    lock_len = len(new_lock) // 3 # 자물쇠의 크기를 변환하기 전, 원래 자물쇠의 크기
    for i in range(lock_len, lock_len * 2): # 중간 부분 확인
        for j in range(lock_len, lock_len * 2): # 중간 부분 확인
            if new_lock[i][j] != 1: # 1이 아니라면 (2일 때는 돌기 부분이 겹치고, 0일때는 홈 부분이 겹침)
                return False
    
    return True


def solution(key, lock):
    answer = False
    
    n = len(lock)
    m = len(key)
    
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    
    # 새로운 자물쇠의 중앙 부분에 기존 자물쇠 대입
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
    
    # 4가지 회전 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_matrix(key) # 열쇠 회전
        
        # 새로운 자물쇠의 index 0 ~ (n * 2)까지 범위에 열쇠를 대입
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠를 끼워넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                
                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True:
                    answer = True
                    break
                
                # 자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    
    return answer
