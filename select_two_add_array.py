
def solution(arr):
    n = len(arr)
    added_list = []
    for i in range(n):
        for j in range(i + 1, n):
            added_list.append(arr[i] + arr[j])
    
    result = sorted(set(added_list))
    return result

arr_1 = [2,1,3,4,1]
arr_2 = [5,0,2,7]

print(solution(arr_1)) 
print(solution(arr_2))