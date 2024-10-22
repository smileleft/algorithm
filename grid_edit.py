# input and result example
# 8,2,["D2","C","U3","C","D4","C","U2","Z","Z"] -> "OOOOXOOO"
# 8,2,["D2","C","U3","C","D4","C","U2","Z","Z","U1","C"] -> "OOXOXOOO"
# result: deleted row = X, same as first = O


def solution(n, c, cmds):

    grid = ["O"] * n
    #for i in range(n):
    #    grid.append("O")

    deleted = []
    current = c

    for cmd in cmds:
        
        if cmd[0] == "D":
            current += int(cmd[1])
        elif cmd[0] == "U":
            current -= int(cmd[1])
        elif cmd[0] == "C":
            current += 0
            deleted.append(current)
            grid[current] = "X"
            if current == n - 1:
                current -= 1
        elif cmd[0] == "Z":
            last_deleted = deleted.pop()
            grid[last_deleted] = "O"

    print(grid)




solution(8,2,["D2","C","U3","C","D4","C","U2","Z","Z"])
#solution(8,2,["D2","C","U3","C","D4","C","U2","Z","Z","U1","C"])
