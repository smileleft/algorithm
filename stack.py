stack = []
max_size = 10

def isFull(stack):
    return len(stack) == max_size


def isEmpty(stack):
    return len(stack) == 0


def push(stack, item):
    if isFull(stack):
        print("Stack is Full")
    else:
        stack.append(item)
        print("Data appended")


def pop(stack):
    if isEmpty(stack):
        print("Stack is Empty")
        return None
    else:
        return stack.pop()
    

