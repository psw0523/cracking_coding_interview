class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, val):
        node = Node(val)
        if self.head is None:
            self.head = self.tail = node 
        elif self.head == self.tail:
            self.tail = node
            self.head.next = self.tail
        else:
            self.tail.next = node
            self.tail = node

    def __iter__(self):
        self.cur = self.head
        return self

    def __next__(self):
        if self.cur != None:
            val = self.cur.val
            self.cur = self.cur.next
            return val
        else:
            raise StopIteration

    def remove_duplicate(self):
        if self.head == None:
            return

        s = set()
        
        cur = self.head
        s.add(cur.val)

        while cur and cur.next:
            if cur.next.val not in s:
                s.add(cur.next.val)
                cur = cur.next
            else:
                cur.next = cur.next.next


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add(9)
    linked_list.add(9)
    linked_list.add(9)
    linked_list.add(10)
    linked_list.add(11)

    for v in linked_list:
        print(v)

    linked_list.remove_duplicate()

    for v in linked_list:
        print(v)
