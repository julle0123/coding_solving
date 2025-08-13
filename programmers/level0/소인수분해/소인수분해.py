def solution(n):
    answer = []
    i=2
    while i<=n:
        if(n%i==0):
            answer.append(i)
            n //= i
        else:
            i+=1
    set_data = set(answer)   
    list_data = list(set_data)     
    list_data.sort()
    return list_data