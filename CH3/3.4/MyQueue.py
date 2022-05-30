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


class MyQueue():
    def __init__(self):
        self.stacks = list()
        self.stacks.append(Stack(1000))
        self.stacks.append(Stack(1000))
        self.qs = self.stacks[0]
        self.dqs = self.stacks[1]

    def enqueue(self, val):
        while self.dqs.is_empty() is False:
            self.qs.push(self.dqs.pop())
        self.qs.push(val)
        while self.qs.is_empty() is False:
            self.dqs.push(self.qs.pop())

    def dequeue(self):
        return self.dqs.pop()

    def is_empty(self):
        return self.dqs.is_empty()

    def peek(self):
        return self.dqs.peek()


if __name__ == '__main__':
    my_queue = MyQueue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.enqueue(4)
    my_queue.enqueue(5)
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
