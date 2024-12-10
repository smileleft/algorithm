#할인 행사

def solution(wants, numbers, discounts):

    wants_list = {}
    i = 0
    for want in wants:
        wants_list[want] = numbers[i]
        i += 1

    print(wants_list)


    result = 0
    for i in range(len(discounts)):
        dic = {}
        if len(discounts) - (i + 1) >= 10:
            items = discounts[i:i+10]
            for item in items:
                if item in dic:
                    dic[item] += 1
                else:
                    dic[item] = 1
            print(dic)
            ok = True
            for key in wants_list.keys():
                if key in dic.keys() and wants_list[key] > dic[key]:
                    ok = False
            if ok == True:
                result += 1

    return result
            

            

        
        # dic = {}
        # for item in items:
        #     if dic[item] in dic:
        #         dic[item] += 1
        #     else:
        #         dic[item] = 1
        

wants = ["banana", "apple", "rice", "pork", "pot"]
numbers = [3,2,2,2,1]
dicsounts = ["chicken","apple","apple","banana","rice",
             "apple","pork","banana","pork","rice","pot",
             "banana","apple","banana"]

print(solution(wants, numbers, dicsounts))