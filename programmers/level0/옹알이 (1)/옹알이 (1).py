def solution(babbling):
    answer = 0    
    a = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        result =0
        for j in range(4):
            if i.find(a[j]) != -1:
                result += len(a[j])
        if len(i) == result:
            answer +=1
    return answer