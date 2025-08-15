def solution(a, b, n):
    answer = 0
    trash=0
    while n>=a:
        trash = n%a
        n = (n//a)*b
        answer +=n
        n = n+trash
    
    return answer