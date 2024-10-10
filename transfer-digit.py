
def solution(input:int):

    bin_list = []
    a = int(input / 2)
    b = input % 2
    bin_list.append(b)

    while a != 0:
        b = a % 2
        bin_list.append(b)
        a = int(a / 2)

    print(bin_list)

input = 3
solution(input)
