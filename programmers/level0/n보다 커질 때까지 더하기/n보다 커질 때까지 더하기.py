def solution(numbers, n):
    answer = 0
    i = 0
    while True :
        if answer > n :
            break
        else:
            answer += numbers[i]
            i+=1
    return answer