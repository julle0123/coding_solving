def solution(cipher, code):
    answer = ''
    answer = cipher[code-1:len(cipher)+1:code]
    return answer