import heapq
def solution(k, score):
    result = []
    answer = []
    for i in range(len(score)):
        heapq.heappush(answer, score[i])
        
        if len(answer) > k :
            heapq.heappop(answer)
            
        result.append(answer[0])          
    return result