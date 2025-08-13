def solution(emergency):
    #answer = emergency
    answer = []
    answer = sorted(emergency,reverse=True)
    cnt = []
    for i in emergency:
        cnt.append(answer.index(i)+1)
        
    return cnt