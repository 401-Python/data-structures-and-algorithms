from stacks_and_queues import Node, Stack, Queue

def test_push():
  test_stack = Stack()
  test_stack.push(1)
  test_stack.push(2)
  assert test_stack.top.value == 2

def test_muliple_nodes():
  test_stack = Stack()
  test_stack.push(1)
  test_stack.push(2)
  test_stack.push(3)
  assert test_stack.length == 3

def test_pop():
  test_stack = Stack()
  test_stack.push(1)
  test_stack.push(2)
  test_stack.push(3)
  popped = test_stack.pop()
  assert popped == 3
  assert test_stack.length == 2
  assert test_stack.top.value == 2

def test_multipop():
  test_stack = Stack()
  test_stack.push(1)
  test_stack.push(2)
  test_stack.push(3)
  test_stack.pop()
  test_stack.pop()
  test_stack.pop()
  assert test_stack.length == 0
  assert test_stack.bottom == None

def test_peek():
  test_stack = Stack()
  test_stack.push(1)
  test_stack.push(2)
  test_stack.push(3)

  assert test_stack.peek() == 3

def test_enqueue():
  q = Queue()
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)

  assert q.front == 1

def test_enqueue_multiple():
  q = Queue()
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)

  assert q.length == 3

def test_dequeue():
  q = Queue()
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)
  q.dequeue()

  assert q.length == 2
  assert q.front == 2

# def test_enqueue_empty_queue():
#   q = Queue()
#   q.enqueue(1)
#   q.enqueue(2)
#   q.enqueue(3)
#   q.dequeue()
#   q.dequeue()
#   q.dequeue()

#   assert q.length == 0

def test_instantiate_empty():
  q = Queue()
  
  assert q.length == 0
  assert q.front == None


def test_q_peek():
  q = Queue()
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3) 
  
  assert q.peek() == 1

