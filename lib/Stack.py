class Stack:

    def __init__(self, items = [], limit = 100):
        self.items=items
        self.limit=limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
           print("Stack is full.Cannot push item.")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Stack is empty. Cannot pop item.")


    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("Stack is empty. Cannot peek item.")


    def size(self):
        length=len(self.items)
        return length

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == target:
                return len(self.items) - i - 1
        return -1
