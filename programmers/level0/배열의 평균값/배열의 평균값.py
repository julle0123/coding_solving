def solution(numbers):
    answer = 0
    sum1=0
    for i in range(len(numbers)):
        sum1 += numbers[i]
    answer = sum1/len(numbers)
    return answer