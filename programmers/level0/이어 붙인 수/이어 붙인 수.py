def solution(num_list):
    answer = ''
    answer1 = ''
    for i in range(len(num_list)):
        if num_list[i] % 2 ==1:
            answer += str(num_list[i])
        else : 
            answer1 += str(num_list[i])
    return int(answer)+int(answer1)