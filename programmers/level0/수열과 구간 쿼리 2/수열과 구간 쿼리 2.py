def solution(arr, queries):
    answer = []   
    
    for i in range(len(queries)) :
        center = []
        a = queries[i][0]
        b = queries[i][1]
        c = queries[i][2]
        
        for j in range(a, b + 1) :
            if arr[j] > c :
                center.append(arr[j])
        try :
            answer.append(min(center))
        except:
            answer.append(-1)
    
    return answer