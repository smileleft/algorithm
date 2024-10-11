
def solution(N, stages):

    # count & # calculate failure ratio
    n = len(stages)
    #result = [0.0] * N
    result = {}
    
    for i in range(1, N + 1):
        count = 0
        fail = 0
        for stage in stages:
            if stage >= i:
                count += 1
            if stage == i:
                fail += 1
        
        result[i] = fail/count
        
    
    # sort and print
    #sorted_result = sorted(result, reverse=True)
    #print(sorted_result)
    #for index, value in enumerate(sorted_result):
    #    print(index + 1)
    return_result = sorted(result, key=lambda x: result[x], reverse=True)
    

    return return_result


print(solution(5, [2,1,2,6,2,4,3,3]))
#print(solution(4, [4,4,4,4,4]))
