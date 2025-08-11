def solution(my_string, index_list):
    answer = ''
    for i in range(len(index_list)):
        answer += my_string.replace(my_string, my_string[index_list[i]])
    return answer