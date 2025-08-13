def solution(number, limit, power):
    answer = 0
    a = []
    for i in range(number+1):
        cnt = 0
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                cnt += 1
                if j != i // j: 
                    cnt += 1
        a.append(cnt)
    for k in range(len(a)):
        if(a[k] <= limit):
            answer +=a[k]
        else:
            answer +=power
    return answer