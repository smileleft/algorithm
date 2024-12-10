# 완주하지 못한 선수

def polynomial_hash(str):
    p = 31
    m = 1_000_000_007
    hash_value = 0
    for char in str:
        hash_value = (hash_value * p + ord(char)) % m
    
    return hash_value


def solution(players, completes):
    hash_completes_list = [polynomial_hash(complete) for complete in completes]
    

    results = []
    for player in players:
        hash_player = polynomial_hash(player)
        if hash_player not in hash_completes_list:
            results.append(player)
    
    return results


def solution2(players, completes):
    dic = {}

    for player in players:
        if player in dic:
            dic[player] += 1
        else:
            dic[player] = 1
    
    for complete in completes:
        dic[complete] -= 1

    for key in dic.keys():
        if dic[key] > 0:
            return key



print(solution2(["leo", "kiki", "eden"], ["eden", "kiki"]))
#print(solution2(["marina","joshep","nikola","vinko","phillip"], ["joshep","phillip","marina","nikola"]))