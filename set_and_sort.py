
def solution(arr):
    set_from_arr = set(arr)
    sorted_arr = sorted(set_from_arr)

    return sorted_arr

arr = [1, 2, 3, 4, 3, 2, 1, 3, 3, 3, 4, 4, 4]
print(solution(arr)) # [1, 2, 3, 4]