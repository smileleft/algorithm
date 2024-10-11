import itertools

def solution(arr):

    print("answer : ", arr)
    
    n = len(arr)
    num_of_selection = 5
    first_appliant = []
    second_appliant = []
    second_answer_list = itertools.cycle([2,1, 2,3, 2,4, 2,5])
    third_appliant = []
    third_answer_list = itertools.cycle([3,3,1,1,2,2,4,4,5,5])

    first_point = 0
    second_point = 0
    third_point = 0

    for i in range(n):
        # confirm applyer's input
        first_appliant.append(i%num_of_selection + 1)
        second_appliant.append(second_answer_list.__next__())
        third_appliant.append(third_answer_list.__next__())

        # calculate num of correct answer
        if arr[i] == first_appliant[i]:
            first_point += 1
        
        if arr[i] == second_appliant[i]:
            second_point += 1

        if arr[i] == third_appliant[i]:
            third_point += 1

    # print answer list
    print("first :  ", first_appliant)
    print("second : ", second_appliant)
    print("third :  ", third_appliant)


    # make result list
    result = dict()
    result['first'] = first_point
    result['second'] = second_point
    result['third'] = third_point

    print(result)

arr = [1, 2, 3, 4, 3, 2, 1, 3, 3, 3, 4, 4, 4]

solution(arr)