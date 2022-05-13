import bisect  

def words_match(words, value): # 키워드별로 매치된 단어의 개수를 세는 함수
    idx = value.find('?') # '?' 문자가 키워드의 접두사에 존재하는지 접미사에 존재하는지 체크
    cnt = value.count('?') # '?' 문자가 키워드에서 몇 개 존재하는지 개수 체크
    new_words = [0] * len(words) # 자르고 새로만든 words 리스트를 저장하는 리스트
    
    if idx == 0 and cnt == len(value): # '?' 문자가 단어 전체인 경우
        new_value = len(value) # value의 길이를 저장
        for i in range(len(words)):
            new_words[i] = len(words[i]) # 해당 문자의 길이를 저장
    elif idx == 0: # '?' 문자가 접두사에 존재할 경우
        new_value = value.replace("?", "") # value 값에서 '?' 문자 제거
        for i in range(len(words)):
            new_words[i] = words[i][cnt:] # 해당 문자에서 앞부분을 cnt개 만큼 자르고 다시 저장
    else: # '?' 문자가 접미사에 존재할 경우
        new_value = value.replace("?", "") # value 값에서 '?' 문자 제거
        for i in range(len(words)):
            new_words[i] = words[i][:len(words[i]) - cnt] # 해당 문자에서 뒷부분을 cnt개 만큼 자르고 다시 저장

    new_words.sort() # 알파벳, 단어의 길이를 오름차순으로 정렬
    
    left_index = bisect.bisect_left(new_words, new_value)
    right_index = bisect.bisect_right(new_words, new_value)
    
    return right_index - left_index
    

def solution(words, queries):
    answer = []
    
    for i in range(len(queries)):
        temp = words_match(words, queries[i])
        answer.append(temp)
    
    return answer

# 현재 코드는 미완성
# 프로그래머스 채점 결과 
# 정확성 : 14.0
# 효율성 : 30.0
# 합계 : 44.0 / 100.0