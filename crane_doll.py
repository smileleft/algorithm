
def solution(board, moves):
    stacks = []

    numRow = len(board)
    numCol = len(board[0])
    print(numRow, numCol)

    for i in range(numRow):
        stack = []
        for j in range(numCol):
            #stack.append(board[numRow - i - 1][j])
            if board[numCol - j - 1][i] != 0:
                stack.append(board[numCol - j - 1][i])
        stacks.append(stack)


    print(stacks)

    result = []
    last_selection = []
    count_away = 0
    
    for m in moves:
        if len(stacks[m - 1]) > 0:
            selection = stacks[m - 1].pop()
            #print(selection)

            if len(last_selection) > 0 and selection == last_selection[-1]:
                result.pop()
                last_selection.pop()
                count_away += 2
            else:
                result.append(selection)
                last_selection.append(selection)

            # check
            if len(result) >= 2 and result[-2] == result[-1]:
                result.pop()
                result.pop()
                count_away += 2

    #print(result)
    print(count_away)
        

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

solution(board, moves)