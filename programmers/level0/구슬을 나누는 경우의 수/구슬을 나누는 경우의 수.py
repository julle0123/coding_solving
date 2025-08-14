def solution(balls, share):
    answer = 1
    result = 1
    ques = 1
    correct = 0
    i=1;
    j=1;
    k=1;
    for i in range(1, balls + 1):
        answer *=i
        i+=1
        
    for i in range(1, balls-share + 1):
        result *=j
        j+=1
    
    for i in range(1, share + 1):
        ques *= k
        k+=1
        
    correct = answer / (result*ques)
    return correct