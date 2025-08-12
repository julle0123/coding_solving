def solution(number):
    answer = 0
    intnum = int(number) % 9
    
    for i in range(len(number)):
        answer += int(number[i])
    
    answer = answer%9
    if intnum == answer :
        answer = answer
    return answer