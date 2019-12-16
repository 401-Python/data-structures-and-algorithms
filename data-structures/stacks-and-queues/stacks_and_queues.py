class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'{self.value}'


class Stack:

  def __init__(self):
      self.top = None
      self.bottom = None
      self.length = 0

  def push(self, value):
      node = Node(value)
      node.next = self.top
      self.top = node
      self.length += 1

  def pop(self):
      if self.length <= 0:
          print('nothing to pop')
          return
      popped = None
      temp = self.top
      self.top = self.top.next
      popped = temp.value
      self.length -= 1
      return popped

  def peek(self):
      if self.length <= 0:
          print('nothing to peek')
          return
      print(self.top.value)
      return self.top.value


class Queue:
  def __init__(self):
    self.front = None
    self.back = None
    self.queue = []
    self.length = 0
  

  def enqueue(self, value):
    self.queue.append(value)
    self.front = self.queue[0]
    self.length+= 1
  

  def dequeue(self):
    shifted = self.queue.pop(0)
    self.front = self.queue[0] or None
    self.length-=1
    return shifted
  

  def peek(self):
    
    return self.front
