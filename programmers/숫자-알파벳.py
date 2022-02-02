def solution(s):
    word = ['zero','one','two','three','four','five','six','seven','eight',
           'nine']
    for i,j in enumerate(word):
        if j in s:
            s = s.replace(j,str(i))
        
    answer = s
    return answer
