

def solution(prices):
    
    n = len(prices)
    count = [0] * n
    stack = [0]
    
    for i in range(1, n):
    
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            count[j] = i - j
        stack.append(i)

    while stack:
        j = stack.pop()
        count[j] = n - 1 - j


    return count

        

prices = [1,2,3,2,3]


print(solution(prices))     