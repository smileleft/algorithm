# 메뉴 리뉴얼
from itertools import combinations
from collections import Counter



def solution(orders, course):
    answer = []

    for c in course:
        menu = []
        for order in orders:
            comb = combinations(sorted(order), c)
            menu += comb
    
    counter = Counter(menu)
    if len(counter) != 0 and max(counter.values()) != 1:
        for m, cnt in counter.items():
            if cnt == max(counter.values()):
                answer.append("".join(m))


    return answer


["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"] [2,3,4] ["AC", "ACDE", "BCFG", "CDE"]
["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"] [2,3,5] ["ACD", "AD", "ADE", "CD", "XYZ"]
["XYZ", "XWY", "WXA"] [2,3,4] ["WX","XY"] 