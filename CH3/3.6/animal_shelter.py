class Queue():
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


class Dog():
    def __init__(self, name):
        self.name = name


class Cat():
    def __init__(self, name):
        self.name = name


class AnimalShelter():
    def __init__(self):
        self.queue = Queue(1000)
        self.dog_queue = Queue(1000)
        self.cat_queue = Queue(1000)

    def enqueue(self, animal):
        if type(animal) is Dog:
            self.queue.queue(animal)
        elif type(animal) is Cat:
            self.queue.queue(animal)
        else:
            raise ValueError('This shelter can protect only dog or cat')

    def dequeueAny(self):
        animal = self.queue.dequeue()
        if type(animal) is Dog:
            self.dog_queue.dequeue()
        else:
            self.cat_queue.dequeue()
        return animal

    def dequeueDog(self):
        if self.dog_queue.is_empty() is False:
            return self.do_queue.dequeue()

        while type(self.queue.peek()) is Cat:
            self.cat_queue.queue(self.queue.dequeue())

        return self.queue.dequeue()

    def dequeueCat(self):
        pass
