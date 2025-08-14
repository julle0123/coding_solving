def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if all(a in ['0', '5'] for a in str(i)): 
            answer.append(i)
    if len(answer) == 0:
        return [-1]
    else:
        return answer
