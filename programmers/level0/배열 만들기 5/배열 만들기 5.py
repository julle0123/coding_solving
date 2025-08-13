def solution(intStrs, k, s, l):
    answer = []
    result = 0
    for i in range(len(intStrs)):
        result = int(intStrs[i][s:s+l])
        if(result>k):
            answer.append(result)
    return answer