class stack:
    def __init__(self, n):
        self.size = n
        self.stack = [None]*self.size
        self.top = -1

    def isEmpty(self):
        return self.top == -1
    def isFull(self):
        return self.top == self.size-1

    def push(self, ele):
        if self.isFull():
            print('stack overflow')
            return
        self.top +=1
        self.stack[self.top] = ele
        print('item pushed successfully')

    def pop(self):
        if self.isEmpty():
            print('stack underflow')
            return
        item , self.top = self.stack[self.top], self.top-1
        return item
    def peek(self):
        if self.isEmpty():
            print('stack underflow')
            return
        return self.stack[self.top]
    def display(self):
        if self.isEmpty():
            print("Empty stack")
        else:
            for i in range(self.top,-1,-1):
                print(self.stack[i])

n = int(input("Enter stack size: "))

s = stack(n)

while True:
    print("\n----- STACK MENU -----")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Check Empty")
    print("6. Check Full")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        ele = int(input("Enter element: "))
        s.push(ele)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.peek()

    elif choice == 4:
        s.display()

    elif choice == 5:
        if s.isEmpty():
            print("Stack is empty")
        else:
            print("Stack is not empty")

    elif choice == 6:
        if s.isFull():
            print("Stack is full")
        else:
            print("Stack is not full")

    elif choice == 7:
        print("Program terminated")
        break

    else:
        print("Invalid choice")