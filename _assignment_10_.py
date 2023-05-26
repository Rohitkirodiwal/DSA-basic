# Q10. Write a program to find the smallest number using a stack.

class Stack:
    def __init__(self):
        self.items = []
        self.min_items = []

    def push(self, val):
        self.items.append(val)

        if not self.min_items or val <= self.min_items[-1]:
            self.min_items.append(val)


    def pop(self):
        item =  self.items.pop()
        if item in self.min_items[-1]:
            self.min_items.pop()
        return item

    
    def is_empty(self):
        return len(self.items) == 0
    
    def smallest_number(self):
        return self.min_items[-1] if self.min_items else None        

    
obj = Stack()
obj.push(135)
obj.push(109)
obj.push(130)

print(obj.items)
print(obj.smallest_number())