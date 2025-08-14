def solution(code):
    answer = ''
    mode = False
    for idx in range(len(code)):
        if mode == 0 :
            if code[idx] == '1':
                mode = True
            else : 
                if idx % 2 == 0:
                    answer += code[idx]
        else :
            if code[idx] == '1':
                mode = False
            else :
                if idx % 2 ==1:
                    answer += code[idx]
    if answer== '':
        return "EMPTY"
    return answer