class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'{self.value}'


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

        self.length = 0

    '''Adds node to head of linked list'''

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    '''Takes in a target value and iterates through Linked List
    until the value is found, or the end of the list is reached
    returns a boolean'''

    def includes(self, value):
        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next

        return False

    def __str__(self):
        values = ''
        current = self.head
        while current:
            values += f'Node: {str(current.value)} '
            current = current.next
        return values

    '''Iterates to the end of a Linked List and appends a value'''

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return
        last = self.head

        while last.next:
            last = last.next

        last.next = new_node

    '''Takes in an existing val and a val to be inserted
    iterates until the existing val is found and reassigns
    pointers to insert the new node before the existing node'''

    def insert_before(self, exisiting_value, new_value):
        new_node = Node(new_value)
        current = self.head
        
        while current.next:
            if current.next.value == exisiting_value:
                new_node.next = current.next
                current.next = new_node
                return
            else:
                current = current.next

    '''Takes in an existing val and a val to be inserted
    iterates until the existing val is found and reassigns
    pointers to insert the new node after the existing node'''

    def insert_after(self, existing_value, new_value):
      new_node = Node(new_value)
      current = self.head
      while current:
        if current.value == existing_value:

          old_node = current.next
          current.next = new_node
          new_node.next = old_node

          return
        else:
          current = current.next

