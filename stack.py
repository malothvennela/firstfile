def stack_arrya(Here are the implementations of a stack using an array and a linked list in Python:
Array Implementation
class ArrayStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = [None] * max_size
        self.top = -1
    def push(self, item):
        if self.top == self.max_size - 1:
            print("Stack is full. Cannot push item.")
            return
        self.top += 1
        self.stack[self.top] = item
    def pop(self):
        if self.top == -1:
            print("Stack is empty. Cannot pop item.")
            return
        item = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return item
    def peek(self):
        if self.top == -1:
            print("Stack is empty.")
            return
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

    def size(self):
        return self.top + 1

Example usage:
array_stack = ArrayStack(5)
array_stack.push(1)
array_stack.push(2)
array_stack.push(3)
print(array_stack.peek())  # 3
print(array_stack.size())  # 3
array_stack.pop()
print(array_stack.size())  # 2
print(array_stack.is_empty())  # False


Linked List Implementation

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None

    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node
    def pop(self):
        if self.top is None:
            print("Stack is empty. Cannot pop item.")
            return
        item = self.top.item
        self.top = self.top.next
        return item
    def peek(self):
        if self.top is None:
            print("Stack is empty.")
            return
        return self.top.item
    def is_empty(self):
        return self.top is None
    def size(self):
        count = 0
        current = self.top
        while current is not None:
            count += 1
            current = current.next
        return count
