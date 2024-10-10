def isValidBraces(braces):
    big_brace = []
    mid_brace = []
    small_brace = []

    for brace in braces:
        if brace == "{":
            big_brace.append("{")
        if brace == "[":
            mid_brace.append("[")
        if brace == "(":
            small_brace.append("(")

        if brace == "}":
            if len(big_brace) != 0:
                big_brace.pop()
            else:
                return False
        if brace == "]":
            if len(mid_brace) != 0:
                mid_brace.pop()
            else:
                return False
        if brace == ")":
            if len(small_brace) != 0:
                small_brace.pop()
            else:
                return False
            
    if len(big_brace) == 0 and len(mid_brace) == 0 and len(small_brace) == 0:
        return True
    else:
        return False
        


def solution(braces):
    
    src = list(braces)
    len_of_input = len(src)
    count = 0
    # move position(rotate braces)
    for i in range(len_of_input):
        b = src[0]
        del src[0]
        src.append(b)
        print(src)
        if isValidBraces(src):
            count += 1
    
    return count

braces = "[](){}"
#braces = "}]()[{"
#braces = "[)(]"
#braces = "}}}"

#print(isValidBraces(braces))
print(solution(braces))
