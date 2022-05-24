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

        return self


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


    def __str__(self):
        cur = self.head
        l = list()

        while cur != None:
            l.append(str(cur.val))
            cur = cur.next

        return ''.join(l)


    def remove_duplicate(self):
        if self.head == None:
            return self

        s = set()
        
        cur = self.head
        s.add(cur.val)

        while cur and cur.next:
            if cur.next.val not in s:
                s.add(cur.next.val)
                cur = cur.next
            else:
                cur.next = cur.next.next

        return self


    def find_from_back(self, k):
        '''find kth element from back
        '''
        cur = self.head
        kth = None
        n = 1
        while cur:
            if n == k:
                kth = self.head
                break
            cur = cur.next
            n += 1

        if kth is None:
            return None

        while cur != self.tail:
            cur = cur.next
            kth = kth.next

        return kth.val


if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.add(1).add(2).add(3).add(4).add(5)
    print(linked_list)
    print(linked_list.find_from_back(5))

