from collections import deque

def solution(progresses, speeds):
    
    #curr_works = deque(range(len(progresses)))
    completed_work = []
    results = []
    
    for i in range(0, len(progresses)):
        cycle_to_complete = int((100 - progresses[i])/speeds[i])
        if (100 - (progresses[i] + speeds[i]  * cycle_to_complete)) > 0:
            cycle_to_complete += 1
        completed_work.append(cycle_to_complete)
        
    print(completed_work)
        
    #for _ in range(len(completed_work)):
    # while len(completed_work) > 1:
    #     result = 1
    #     # [5, 10, 1, 1, 20, 1]
    #     last_value = completed_work.pop() 
    #     if last_value >= completed_work[0]:
    #         result += 1
    #         continue
    #     else:
    #         results.append(result)
    
    result = 0
    last_value = completed_work[0]
    for i in range(len(completed_work)):
        if completed_work[i] <= last_value:
            result += 1
        else:
            results.append(result)
            result = 1
            last_value = completed_work[i]
            
    results.append(result)
        
            
            
    print(results)
            

def solutions(progresses, speeds):
    
    curr_index = 0
    results = []
    
    while len(progresses) > 0:
        curr_index += 1
        result = 0
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + (speeds[i] * curr_index)
            if progresses[i] > 100:
                result += 1
    
    


solution([93,30,55], [1,30,5])
#solution([95,90,99,99,80,99], [1,1,1,1,1,1])