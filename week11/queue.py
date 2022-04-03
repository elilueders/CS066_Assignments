class Stack:
    def __init__(self):
        self.items = []

    def __repr__(self):
        return str(self.items)

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)



my_stack = Stack()
my_stack.push(4)
my_stack.push(7)
my_stack.push(11)
my_stack.pop()
my_stack.push(8)
my_stack.pop()
my_stack.push(5)
print(my_stack.peek())
my_stack.push(9)

print("Size:",my_stack.size())
print(my_stack)



# abstract data type = description of 
# data structure = implementation