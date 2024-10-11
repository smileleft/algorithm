def deleteTwins(target:list, start_index:int):
    result = target
    del result[start_index, start_index + 1]
    return result

def answer(s):
    stack = []
    for c in s:
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)

    return int(not stack) 


def solution(input:str):
    strings = list(input)
    twins_list = []
    i = 0
    while len(strings) > 0:
        if len(strings) == 0 or i == len(strings) - 1:
            break

        if strings[i] == strings[i+1]:
            del strings[i:i+2]
            i = 0
        else:
            i += 1

        

    if len(strings) == 0:
        return 1
    else:
        return 0
    

#inputs = "baabaa"
inputs = "cdcd"

print(solution(inputs))

        