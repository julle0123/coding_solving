def solution(arr):
    answer = []
    result = [-1]
    for i in range(len(arr)):
        if arr[i]==2 :
            answer.append(i)
            result = arr[answer[0]:answer[-1]+1] 
            
    return result