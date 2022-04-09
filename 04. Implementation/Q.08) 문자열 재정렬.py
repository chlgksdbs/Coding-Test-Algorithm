s = input()
new_str = []
s_sum = 0

for x in s:
    if int(ord(x)) - int(ord('A')) >= 0: # 해당 문자가 대소문자라면,
        new_str.append(x) # 새로운 str 리스트에 해당 문자를 추가
    else: # 해당 문자가 숫자라면,
        s_sum += int(x) # 해당 숫자를 int형으로 변환한 뒤, s_sum에 그 값을 더함

new_str.sort() # 대소문자로 구성된 리스트를 사전순으로 오름차순 정렬
if s_sum != 0:
    new_str.append(s_sum) # 위에서 구한 값을 새로운 str 리스트 뒤에 추가

for z in new_str: # 출력 (print(''.join(result))) 로 간단히 출력가능
    print(z, end="")

# 문자열이 입력되었을 때 문자를 하나씩 확인한다.
# 숫자인 경우 따로 합계를 계산한다
# 알파벳의 경우 별도의 리스트에 저장한다.
# 결과적으로 리스트에 저장된 알파벳을 정렬해 출력하고, 합계를 뒤에 붙여 출력하면 정답

# 숫자가 입력되지 않았을 때를 위해 12번째 line에 있는 조건문을 필수!!!
# 위 조건문없이 실행할 때에 s_sum의 값이 0일 때도 출력이 된다.
