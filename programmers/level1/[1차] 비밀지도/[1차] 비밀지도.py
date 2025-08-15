def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        #answer.append(arr1[i] | arr2[i])
        temp = bin(arr1[i] | arr2[i])
        temp = temp[2:].zfill(n)
        #answer[i] = answer[i].replace("0b", "")
        temp = temp.replace("1", "#")
        temp = temp.replace("0", " ")
        answer.append(temp)
    return answer