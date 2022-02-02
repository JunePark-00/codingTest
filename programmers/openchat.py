#프로그래머스 - 오픈채팅방
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
        
def solution(record):
    answer = []
    nick = {}
    for i in record:
        command = i.split()
        # id에 닉네임 저장
        if(command[0]=='Enter' or command[0]=='Change'):
            nick[command[1]] = command[2]
    for i in record:
        command = i.split()
        if(command[0]=='Enter'):
            answer.append(f'{nick[command[1]]}님이 들어왔습니다.')
        elif(command[0]=='Leave'):
            answer.append(f'{nick[command[1]]}님이 나갔습니다.')
    return answer

solution(record)
