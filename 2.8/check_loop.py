class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, node):
        if self.head is None:
            self.head = self.tail = node 
        elif self.head == self.tail:
            self.tail = node
            self.head.next = self.tail
        else:
            self.tail.next = node
            self.tail = node

        return self

    def add(self, val):
        node = Node(val)
        return self.add_node(node)

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

        return '->'.join(l)

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

    def del_mid(self):
        if self.head != None and self.head != self.tail and self.head.next != self.tail:
            self.head.next = self.head.next.next
        return self

    def arrange(self, val):
        # if Node.val < val, arrange to left side of that node
        # 1. go to the Node having the val
        # 2. cur is next of found Node
        # 3. Go through tail, if val of cur is less than val, remove
        # 4. always refer to cur->next
        cur = self.head
        while cur and cur.val != val:
            cur = cur.next

        if cur is None:
            return self

        while cur.next != None:
            if cur.next.val < val:
                # move cur.next to head
                # 1. backup
                next_node = cur.next.next
                # 2. change head
                cur.next.next = self.head
                self.head = cur.next
                # 3. remove 
                cur.next = next_node
            else:
                cur = cur.next

        return self

    def __add__(self, other):
        me = self.head
        you = other.head
        carry = 0
        added = LinkedList()

        while me or you:
            my_val = 0
            your_val = 0
            me_next = None
            you_next = None
            if me:
                my_val = me.val
                me_next = me.next
            if you:
                your_val = you.val
                you_next = you.next
            val = my_val + your_val + carry
            if val >= 10:
                val -= 10
                carry = 1
            else:
                carry = 0

            added.add(val)
            me = me_next
            you = you_next

        return added

    def reverse(self):
        reversed_list = LinkedList()
        for v in self:
            head = reversed_list.head
            if head == None:
                reversed_list.add(v)
            else:
                node = Node(v)
                node.next = head
                reversed_list.head = node
        return reversed_list

    def add_reverse(self, other):
        reversed_me = self.reverse()
        print("me: ", reversed_me)
        reversed_other = other.reverse()
        print("other: ", reversed_other)
        return reversed_me + reversed_other

    def is_palindrome(self):
        reversed_me = self.reverse()
        # get length
        length = 0
        cur = self.head
        while cur:
            length += 1
            cur = cur.next

        n = length / 2
        compared = 0
        cur = self.head
        reversed_cur = reversed_me.head
        while compared < n:
            if cur.val != reversed_cur.val:
                return False
            cur = cur.next
            reversed_cur = reversed_cur.next
            compared += 1

        return True

    def intersect(self, other):
        # compare each node is too expensive, O(n^2)
        # use set
        s = set()
        cur = self.head
        while cur:
            s.add(cur)
            cur = cur.next

        intersection = LinkedList()
        cur = other.head
        while cur:
            if cur in s:
                intersection.add_node(cur)
            cur = cur.next

        return intersection

    def check_loop(self):
        # using set, head 부터 set에 추가하면서 만약 next가 set에 있으면 next를 리턴한다.
        s = set()
        cur = self.head

        while cur:
            if cur in s:
                return cur
            s.add(cur)
            cur = cur.next

        return None



if __name__ == '__main__':
    linked_list = LinkedList()
    node = Node('e')
    linked_list.add('a').add('b').add_node(node).add('b').add('a').add_node(node)
    print(linked_list.check_loop())
