
def solution(board, moves):
    stacks = []

    numRow = len(board)
    numCol = len(board[0])
    print(numRow, numCol)

    for i in range(numRow):
        stack = []
        for j in range(numCol):
            stack.append(board[numRow - i - 1][j])

        stacks.append(stack)


    print(stacks)

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

solution(board, moves)