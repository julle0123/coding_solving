def solution(myString, pat):
    answer = 0
    myString = myString.casefold()
    pat = pat.casefold()
    if pat in myString:
        return 1
    else:
        return 0    