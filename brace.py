
def solution(braces:str):

    if len(braces)%2 != 0:
        return False
    
    chk_stack = []
    for brace in braces:
        if brace == '(':
            chk_stack.append(brace)
        
        if brace == ')':
            chk_stack.pop()

    if len(chk_stack) == 0:
        return True
    

print(solution("((())()"))
#print(solution("(())()"))