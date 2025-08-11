def solution(num_list):
    answer = 1
    sum1 = 0
    for i in range(len(num_list)):
        answer *=num_list[i]
        sum1 +=num_list[i]
        
    if answer < sum1 ** 2 :
        return 1
    else:
        return 0
            