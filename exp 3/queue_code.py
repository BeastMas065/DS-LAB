class Queue:
    def __init__(self, size):
        self.q = [None]*size
        self.size = size
        self.front = self.rear = -1

    def isEmpty(self):
        return self.front == -1 or self.front > self.rear 

    def isFull(self):
        return self.rear == self.size - 1

    def enqueue(self, ele):
        if self.isFull():
            print("Overflow")
            return
        if self.isEmpty():
            self.front = 0
        self.rear += 1
        self.q[self.rear] = ele
        print("item inserted")
        return
    
    def dequeue(self, ele):
        if self.isEmpty():
            print("Empty")
            return
        ele = self.q[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front += 1
        print("item deleted")
        return ele

    def peek(self):
        if self.isEmpty():
            print("Empty")
            return
        print(self.q[self.front])

    def display(self):
        if self.isEmpty():
            print("Empty")
            return
        p = self.front
        while p <=self.rear:
            print(self.q[p])