def solution(price, money, count):
    answer = 0
    for i in range(count+1):
        answer+=price*i
    
    if(money < answer):
        return answer-money
    else:
        return 0
