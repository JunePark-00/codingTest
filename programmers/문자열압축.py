# 문자열 압축
# for문으로 문자열 슬라이싱하면서 갯수 세자!
# 쪼갤 수 있는 단위의 최대는 s의 절반이다. 넘어가면 범위초과. 
# 제일 앞부터 정해진 길이로 잘라야하기 때문임
# aabb/accc

s = 'xababcdcdababcdcd'

def solution(s):
    length = []

    if(len(s)==1):
        return 1

    # 1단위로 쪼개기 ~ len(s)//2 단위로 쪼개기
    # 앞 문자(단위)랑 겹치는지 확인
    for i in range(1,(len(s)//2)+1):
        final = ''
        cnt = 1
        temp = s[:i]
        for j in range(i, len(s), i):
            if(temp==s[j:j+i]):
                cnt += 1
            elif(cnt!=1):
                final += str(cnt) + temp
                temp = s[j:j+i]
                cnt = 1
            else:
                final += temp
                temp = s[j:j+i]
                cnt = 1
        if(cnt!=1):
            final += str(cnt) + temp
        else:
            final += temp
        
        length.append(len(final))
        print(final)
    
    answer = min(length)
    return answer
    

solution(s)
