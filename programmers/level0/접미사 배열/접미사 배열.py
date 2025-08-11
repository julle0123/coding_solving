def solution(my_string):
    answer = []
    result = []
    my_string = my_string[::-1]
    for i in range(len(my_string)):
        result = my_string[:i+1:]
        answer.append(result[::-1])
    return sorted(answer)