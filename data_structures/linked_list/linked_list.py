

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

        self.length = 0

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

        def __repr__(self):
            return f'{self.value}'

    '''Adds node to head of linked list'''

    def insert(self, value):
        node = self.Node(value)
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
        print(values)
        return values

    '''Iterates to the end of a Linked List and appends a value'''

    def append(self, value):
        new_node = self.Node(value)
        if self.head == None:
            self.head = new_node
            return
        last = self.head

        while last.next:
            last = last.next

        last.next = new_node
        self.length += 1

    def find(self, value):

        if self.head == None:
            return None

        currentNode = self.head

        while not currentNode == None:

            if currentNode.value == value:
                return currentNode

            currentNode = currentNode.next

        return None

    '''Takes in an existing val and a val to be inserted
    iterates until the existing val is found and reassigns
    pointers to insert the new node before the existing node'''

    def insert_before(self, exisiting_value, new_value):
        new_node = self.Node(new_value)
        current = self.head

        while current.next:
            if current.next.value == exisiting_value:
                new_node.next = current.next
                current.next = new_node
                self.length += 1
                return
            else:
                current = current.next

    '''Takes in an existing val and a val to be inserted
    iterates until the existing val is found and reassigns
    pointers to insert the new node after the existing node'''

    def insert_after(self, existing_value, new_value):
        new_node = self.Node(new_value)
        current = self.head
        while current:
            if current.value == existing_value:

                old_node = current.next
                current.next = new_node
                new_node.next = old_node
                self.length += 1
                return
            else:
                current = current.next

    def kth_from_the_end(self, k):
        current = self.head
        count = 0

        while current.next:
            current = current.next
            count += 1

        if k > count:
            raise Exception('K can not be greater than the lengh of the list')

        current = self.head

        for _ in range(count - k):
            current = current.next
        print(current.value)
        return current.value


def merge(list_a, list_b):
    current_b = list_a.head
    current_a = list_b.head

    while current_a and current_b:

        a_next = current_a.next
        b_next = current_b.next

        current_b.next = a_next
        current_a.next = current_b

        current_a = a_next
        current_b = b_next
    list_b.head = current_b
