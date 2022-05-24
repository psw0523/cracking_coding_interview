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


if __name__ == '__main__':
    st = Stack(1000) 
    st.push(1)
    st.push(2)
    st.push("haha")
    print(st.pop())
    print(st.pop())
    print(st.pop())
