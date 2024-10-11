

def is_valid_move(nx, ny):
    return -5 <= nx <= 5 and -5 <= ny <= 5


def update_position(x, y, command):
    if command == 'U':
        nx, ny = x, y + 1
    if command == 'D':
        nx, ny = x, y - 1
    if command == 'R':
        nx, ny = x + 1, y
    if command == 'L':
        nx, ny = x - 1, y
    return nx, ny


def solution(commands:str):
    
    x, y = 0, 0
    travel_pos = set()

    for command in commands:
        new_x, new_y = update_position(x, y, command)
        if not is_valid_move(new_x, new_y):
            continue

        travel_pos.add((x, y, new_x, new_y))
        travel_pos.add((new_x, new_y, x, y))
        x, y = new_x, new_y
    
    return len(travel_pos)/2

print(solution('ULURRDLLU'))
#print(solution("LULLLLLLU"))
