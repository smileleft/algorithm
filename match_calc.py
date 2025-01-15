# 예상 대진표

def solution(n, a, b):
    answer = 0

    while a != b:
        a = (a+1)//2
        b = (b+1)//2
        answer += 1

    return answer


# 8,4,7 -> 3
# 4
# 4-7
# 2-4, 6-7
# 1-2, 3-4, 5-6, 7-8

print(solution(8,1,4))