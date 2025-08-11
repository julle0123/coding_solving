def solution(myString):
    answer = myString.split("x")
    result = []
    for i in range(len(answer)):
        result.append(len(answer[i]))
    return result