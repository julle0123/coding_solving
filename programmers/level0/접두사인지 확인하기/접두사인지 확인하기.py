def solution(my_string, is_prefix):
    answer = []
    result = ""
    for i in range(len(my_string)):
        answer.append(my_string[:i+1])
    result = sorted(answer) 
    if is_prefix in result :
        return 1
    else:
        return 0
