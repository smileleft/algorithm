#신고  결과 받기

'muzi',1,['frodo', 'neo']
'frodo',2,['neo']
'apeach',0,['frodo', 'muzi']
'neo',2,[]
{'id':{'targetted':0, 'target':[]}}

# 결국 리턴해야 할 리스트는 신고한 계정의 정지처리 갯수
# 같은 사용자를 반복 신고해도 횟수는 1로 계산됨

def solution(id_list, report, k):

    #answer = [{'id':id, 'targetted':0, 'target':[]} for id in id_list]
    #print(answer)
    answer = []

    targets = {id:0 for id in id_list}
    acts = dict()    

    for r in report:
        data = r.split(" ")
        user = data[0]
        target = data[1]
        
        if user not in acts.keys():
            acts[user] = []
            acts[user].append(target)
            targets[target] += 1
            #targets['warn_target'].append(target)
 
        elif user in acts.keys() and target not in acts[user]:
            # 동일한 사용자의 다른 사용자 신고
            acts[user].append(target)
            targets[target] += 1
        else:
            pass
            # 타 사용자의 신고
            #acts[user] = target
            #acts[user].append(target)
            #targets[target] += 1
            #targets['warn_target'].append(target)

    print(targets)
    print(acts)


    for id in id_list:
        result = 0
        if id in acts.keys():
            item_list = acts[id]
            for item in item_list:
                if targets[item] >= k:
                    result += 1
        answer.append(result)

    return answer


    


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
#print(solution(["con", "ryan"], ["ryan con","ryan con","ryan con","ryan con"], 3))
            

