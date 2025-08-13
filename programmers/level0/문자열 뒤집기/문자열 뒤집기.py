def solution(my_string, s, e):
    answer = my_string[s:e+1] 
    my_string =my_string[:s] + answer[::-1] + my_string[e+1:]
    
    return my_string