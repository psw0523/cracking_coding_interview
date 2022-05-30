class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pool = [0] * capacity
        self.top = 0 

    def push(self, item):
        self.pool[self.top] = item
        self.top += 1
        if self.top == self.capacity:
            raise IndexError('over capacity: ', self.capacity)

    def pop(self):
        if self.top == 0:
            return None
        self.top -= 1
        return self.pool[self.top]

    def peek(self):
        if self.top == 0:
            return None
        return self.pool[self.top - 1]

    def is_empty(self):
        return self.top == 0


def sort_stack(stack):
    tmp = Stack(1000)
    tmp.push(stack.pop()) # 2
    while stack.is_empty() is False:
        if stack.peek() <= tmp.peek():
            tmp.push(stack.pop())
        else:
            v = stack.pop()
            while tmp.is_empty() is False and tmp.peek() < v:
                stack.push(tmp.pop())
            tmp.push(v)
    return tmp


if __name__ == '__main__':
    stack = Stack(1000)
    stack.push(7)
    stack.push(8)
    stack.push(1)
    stack.push(3)
    stack.push(6)
    stack.push(2)
    sorted_stack = sort_stack(stack)
    print(sorted_stack.pop())
    print(sorted_stack.pop())
    print(sorted_stack.pop())
    print(sorted_stack.pop())
    print(sorted_stack.pop())
    print(sorted_stack.pop())
