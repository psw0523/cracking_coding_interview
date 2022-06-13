from enum import Enum

class LinkedListQueue():
    def __init__(self):
        self.head = None
        self.tail = None

    def queue(self, item):
        if self.head == None:
            self.head = item
            self.head.next = self.tail
        elif self.tail == None:
            self.tail = item
            self.tail.next = None
        else:
            self.tail.next = item
            self.tail = item
            self.tail.next = None

    def dequeue(self):
        item = None
        if self.head != None:
            item = self.head
            self.head = self.head.next
        return item

    def dequeue_type(self, item_type):
        item = self.head
        prev = item
        while item != None:
            if item.type == item_type:
                if item == self.head:
                    self.head = self.head.next
                else:
                    prev.next = item.next
                break
            prev = item
            item = item.next
        return item

    def peek(self):
        item = None
        if self.head != None:
            item = self.head
        return item

    def is_empty(self):
        return self.head == None

    def __str__(self):
        item = self.head
        s = ''
        while item != None:
            #  s.join(item.name)
            #  s.join('->')
            s = s + item.name
            item = item.next
            if item is not None:
                s = s + ' -> '
        return s


class AnimalType(Enum):
    Dog = 1
    Cat = 2
    Others = 3


class Animal():
    def __init__(self, name, animal_type):
        self.name = name
        self.type = animal_type
        self.next = None

    def __str__(self):
        return self.name


class AnimalShelter():
    def __init__(self):
        self.queue = LinkedListQueue()

    def enqueue(self, animal):
        self.queue.queue(animal)
        if animal.type is AnimalType.Dog or animal.type is AnimalType.Cat:
            self.queue.queue(animal)
        else:
            raise ValueError('This shelter can protect only dog or cat')

    def dequeueAny(self):
        return self.queue.dequeue()

    def dequeueDog(self):
        return self.queue.dequeue_type(AnimalType.Dog)

    def dequeueCat(self):
        return self.queue.dequeue_type(AnimalType.Cat)

if __name__ == '__main__':
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(Animal("dog1", AnimalType.Dog))
    animal_shelter.enqueue(Animal("cat1", AnimalType.Cat))
    animal_shelter.enqueue(Animal("cat2", AnimalType.Cat))
    animal_shelter.enqueue(Animal("dog2", AnimalType.Dog))
    animal_shelter.enqueue(Animal("dog3", AnimalType.Dog))
    animal_shelter.enqueue(Animal("dog4", AnimalType.Dog))
    animal_shelter.enqueue(Animal("dog5", AnimalType.Dog))
    animal_shelter.enqueue(Animal("cat3", AnimalType.Cat))
    animal_shelter.enqueue(Animal("cat4", AnimalType.Cat))
    animal_shelter.enqueue(Animal("cat5", AnimalType.Cat))
    print(animal_shelter.queue)
    print(animal_shelter.dequeueAny())
    print(animal_shelter.dequeueDog())
    print(animal_shelter.dequeueDog())
    print(animal_shelter.dequeueAny())
    print(animal_shelter.dequeueCat())
    print(animal_shelter.dequeueCat())
    print(animal_shelter.dequeueCat())
    print(animal_shelter.dequeueCat())
    print(animal_shelter.dequeueAny())
    print(animal_shelter.dequeueDog())
    print(animal_shelter.dequeueDog())
