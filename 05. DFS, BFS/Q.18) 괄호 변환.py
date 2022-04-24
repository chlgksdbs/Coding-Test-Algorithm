def balanced_str(s): # 균형 잡힌 괄호 문자열을 반환하는 함수
    a = '('
    b = ')'
    count_a = 0 # a 문자의 개수를 세는 변수
    count_b = 0 # b 문자의 개수를 세는 변수
    new_s = "" # s로부터 분리된 균형 잡힌 괄호 문자열을 반환
    
    for x in s:
        if x == a:
            count_a += 1
        else:
            count_b += 1
        
        new_s += x # 새로운 문자열 생성
        
        if count_a != 0 and count_b != 0 and count_a == count_b:
            return new_s

def correct_str_check(s): # 올바른 괄호 문자열인지 체크하는 함수
    a = '('
    b = ')'
    count_a = 0 # a 문자의 개수를 세는 변수
    count_b = 0 # b 문자의 개수를 세는 변수
    
    for x in s:
        if x == a:
            count_a += 1
        else:
            count_b += 1
        
        if count_a < count_b: # '괄호 열기' 문자보다 '괄호 닫기' 문자가 더 많을 경우
            return False
    
    return True

def dfs(s): # 괄호 변환에 대해 재귀적으로 수행하는 함수
    
    if s == "": # (1) 수행
        return s
    
    # (2) 수행
    u = balanced_str(s)
    if u != None:
        v = s.replace(u, "", 1) # 문자열 p에서 문자열 u부분을 제외한 나머지 문자열
    else:
        v = "" # 빈 문자열
    
    new_s = "" # 새로운 문자열
    
    if correct_str_check(u) == True: # (3) 수행
        new_s += u + dfs(v)
    else: # (4) 수행
        new_s += "(" # (4-1) 수행
        new_s += dfs(v) # (4-2) 수행
        new_s += ")" # (4-3) 수행
        u = u[1 : len(u) - 1] # (4-4) 수행
        
        for x in u: # 괄호 방향을 뒤집어서 뒤에 붙힘
            if x == '(':
                new_s += ')'
            else:
                new_s += '('
        
    return new_s

def solution(p):
    answer = ""
    
    if correct_str_check(p): # 이미 올바른 괄호 문자열이거나 빈 문자열이면 입력받은 문자열을 반환
        return p
    else:
        answer += dfs(p)
        return answer
