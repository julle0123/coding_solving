def solution(a, b, c, d):
    answer = 0
    list1 = [a,b,c,d]
    list1.sort()
    if (list1[0]==list1[3]):
        answer = 1111*list1[0]
    elif(list1[0]!=list1[1]and list1[2]==list1[3] and list1[1]==list1[2]):
        answer = (10*list1[1]+list1[0])*(10*list1[1]+list1[0])
    elif(list1[2]!=list1[3]and list1[0]==list1[1] and list1[1]==list1[2]):
        answer = (10*list1[2]+list1[3])*(10*list1[2]+list1[3])
    elif((list1[0]==list1[1])and(list1[2]==list1[3])):
        answer = (list1[0]+list1[3]) * (abs(list1[1]-list1[2]))
    elif((list1[0]==list1[1])and(list1[2]!=list1[3])):
        answer = list1[2]*list1[3]
    elif((list1[1]==list1[2])and(list1[0]!=list1[3])):
        answer = list1[0]*list1[3]
    elif((list1[2]==list1[3])and(list1[0]!=list1[1])):
        answer = list1[0]*list1[1]
    else:
        answer = list1[0]
        
    return answer