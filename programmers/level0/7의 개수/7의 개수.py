def solution(array):
    array = str(array)
    cnt =0
    for i in range(len(array)):
        if array[i] == '7':
            cnt+=1
    
    return cnt