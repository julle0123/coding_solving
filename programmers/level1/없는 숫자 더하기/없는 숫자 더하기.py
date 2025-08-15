def solution(numbers):
    result = 45
    for i in range(0,len(numbers)):
        result -= numbers[i]
        
    return result