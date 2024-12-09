# 두 개의 수 특정값 만들기

def count_sort(arr, k):
    hashtable = [0] * (k+1)

    for num in arr:
        #현재 원소의 값이 k 이하인 때에만 처리
        if num <= k:
            hashtable[num] = 1
    
    return hashtable


def solution(arr, target):
    hashtable = count_sort(arr, target)

    for num in arr:
        complement = target - num

        # target에서 현재 값을 뺀 값이 해시테이블에 있는지 확인
        if (complement != num and complement >= 0 and complement <= target and hashtable[complement] == 1):
            return True
        
    return False
    
#print(solution([1,2,3,4,8], 6))
print(solution([2,3,5,9], 10))