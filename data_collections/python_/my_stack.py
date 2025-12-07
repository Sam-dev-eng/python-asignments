from array import Array


class MyStack:
    def __init__(self):
        self.my_stack = Array(5)
        self.count = 0
        self.get = 0

    def empty(self):
        return self.count == 0

    def peek(self):
        item = self.my_stack[self.get]
        self.get += 1
        return item

    def push(self, value):
        if self.count == len(self.my_stack):
            self.increase_length(len(self.my_stack)* 2)
        self.my_stack[self.count] = value
        self.count += 1

    def search(self, value):
        for index in range(len(self.my_stack)):
            if self.my_stack[index] == value:
                return index
        return -1

    def increase_length(self, value):
        new_stack = Array(value)
        for index in range(len(self.my_stack)):
            new_stack[index] = self.my_stack[index]

        self.my_stack = new_stack



my_stack = MyStack()
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
print(my_stack.peek())

