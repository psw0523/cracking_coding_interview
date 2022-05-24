class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [0] * capacity
        self.head = 0 # head is read position
        self.tail = 0 # tail is write position

    def queue(self, item):
        self.buffer[self.tail] = item
        self.tail += 1
        self.tail %= self.capacity
        if self.tail == self.head:
            raise IndexError('Buffer Overflow')

    def dequeue(self):
        item = None
        if self.head != self.tail:
            item = self.buffer[self.head]
            self.head += 1
            self.head %= self.capacity
        return item

    def peek(self):
        if self.head != self.tail:
            return self.buffer[self.head]
        return None

    def is_empty(self):
        return self.head == self.tail


if __name__ == '__main__':
    q = Queue(1000)
    q.queue(1)
    q.queue(2)
    q.queue(3)
    q.queue("hahaha")
    print(q.is_empty())
    print(q.peek())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
