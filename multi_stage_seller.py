# 다단계 칫솔 판매

class Node:
    def __init__(self):
        self.enroll = None
        self.referral = None
        self.income = 0


def solution(enrolls, referrals, seller, amount):
    answer = []

    nodes = dict()


    #for n, r in enrolls, referrals:
    for i in range(len(enrolls)):
        node = Node()
        node.enroll = enrolls[i]
        if referrals[i] != "-":
            node.referral = referrals[i]
        else:
             node.referral = "center"
        nodes[node.enroll] = node
    
    node_center = Node()
    node_center.enroll = "center"
    nodes["center"] = node_center

    #for s, a in seller, amount:
    for j in range(len(seller)):
        curr_node = nodes[seller[j]]
        curr_node.income += amount[j] * 100 - ( (amount[j] * 100)//10 )
        up_amount = amount[j] * 100 - curr_node.income
        while curr_node.referral != None:
                    #up_amount = curr_node.income//10
                    curr_node = nodes[curr_node.referral]
                    curr_node.income += up_amount - (up_amount//10)
                    up_mount = up_amount//10

    
    #return answer
    return nodes

#answer = solution(["john","mary","edward","sam","emily","jamie","tod","young"],["-","-","mary","edward","mary","mary","jamie","edward"],["young","john","tod","emily","mary"],[12,4,2,5,10])
answer = solution(["john","mary","edward","sam","emily","jamie","tod","young"],["-","-","mary","edward","mary","mary","jamie","tod","young"],["sam","emily","jamie","edward"],[2,3,5,4])
for key in answer.keys():
     print(answer[key].enroll, answer[key].income)
#->[360,958,108,0,450,18,180,1080]
#print(solution(["john","mary","edward","sam","emily","jamie","tod","young"],["-","-","mary","edward","mary","mary","jamie","tod","young"],["sam","emily","jamie","edward"],[2,3,5,4]))
#->[0,110,378,180,270,450,0,0]


