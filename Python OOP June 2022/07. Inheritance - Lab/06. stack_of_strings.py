# 6.Stack of Strings
# Create a class Stack that can store only strings and has the following functionality:
# Instance attribute: data: list
# Method: push(element) – adds an element at the end of the stack
# Method: pop() – removes and returns the last element in the stack
# Method: top() - returns a reference to the topmost element of the stack
# Method: is_empty() - returns boolean True/False
# Override the string method to return the stack data in the format:
# "[{element(N)}, {element(N-1)} ... {element(0)}]"

class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        if isinstance(element, str):
            self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if len(self.data) > 0:
            return False
        else:
            return True

    def __str__(self):
        result = []
        for i in range(len(self.data)-1, -1, -1):
            result.append(self.data[i])
        return f"[{', '.join(result)}]"


stack = Stack()
stack.push(2)
stack.push("3")
stack.push("4")
stack.push("carrot")
print(stack.top())
print(stack.is_empty())
print(stack)
print(stack.top())
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print(stack.is_empty())
