def push(value):
    global top
    if not is_full():
        top = -1
        stack[top] = value
    else:
        print('가득참참')

def pop():
    global top
    if not is_empty():
        value = stack[top]
        top -= 1
        return value

def is_full():
    return top == size-1

def is_empty():
    if top == -1:
        return True
    else:
        return False
    return top == -1

def peek():
    return stack[top]

size = 10
stack = [-1]*size

top = -1
push(3)
print(top,stack)

push(4)
print(top,stack)

push(10)
print(top,stack)

print(pop())
print(top,stack)
