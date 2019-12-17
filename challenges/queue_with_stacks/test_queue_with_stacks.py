from queue_with_stacks import PseudoQueue, Stack, Node

def test_enqueue():
  q = PseudoQueue()
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)

  assert q.main_stack.top.value == 1

def test_dequeue():
  q = PseudoQueue()
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)

  popped = []
  for _ in range(3):
    popped.append(q.dequeue())
  
  assert popped == [1, 2, 3]