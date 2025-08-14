def solution(quiz):
    answer = []
    j = 0
    for i in quiz:
        arr = i.split()
        if arr[1] == "-":
            if(int(arr[0])) - (int(arr[2])) == int(arr[len(arr)-1]) :
                answer.append("O")
            else:
                answer.append("X")
        if arr[1] == "+":
            if(int(arr[0])) + (int(arr[2])) == int(arr[len(arr)-1]) :
                answer.append("O")
            else:
                answer.append("X")        
        
        
        
    return answer