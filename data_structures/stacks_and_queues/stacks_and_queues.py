class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'{self.value}'


class Stack:

    def __init__(self):
        '''initialize stack with top, bottom and length'''
        self.top = None
        self.bottom = None
        self.length = 0
    
    def isEmpty(self):
        return self.top == None

    def push(self, value):
        '''adds new node to top of stack by pointing it to self.top'''
        node = Node(value)
        node.next = self.top
        self.top = node
        self.length += 1

    def pop(self):
        '''Takes item from top of stack and returns it by reassigning the current top
        to the next item in the stack. Stores the value in a temp variable to be returned'''
        if self.length <= 0:
            print('nothing to pop')
            return
        
        temp = self.top
        self.top = self.top.next
        popped = temp.value
        self.length -= 1
        return popped

    def peek(self):
        '''prints and returns the top of the stack'''
        if self.length <= 0:
            print('nothing to peek')
            return
        print(self.top.value)
        return self.top.value


class Queue:

    def __init__(self):
        '''initializes a queue instance'''
        self.front = None
        self.rear = None
        self.length = 0

    def isEmpty(self):
        return self.front == None

    def enqueue(self, value):
        '''appends value to front of queue'''

        self.length += 1
        new_node = Node(value)

        if self.rear == None:
            self.front = self.rear = new_node

            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        '''removes value from front of queue, if length is zero it returns the queue
        and prints a message'''
        self.length -= 1

        if self.isEmpty():
            self.queue = []
            print('queue is empty')
            return self.queue

        temp = self.front
        self.front = temp.next

        if self.front == None:
            self.rear = None

        return str(temp.value)

    def peek(self):
        '''returns the first value in a queue'''
        return self.front.value
