class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return f'{self.val}'


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

        self.length = 0

    def insert(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
        self.length += 1

    def includes(self, val):
        current = self.head
        is_in_list = False
        while current != None:
            if current.val == val:
                is_in_list = True
            current = current.next

        return is_in_list

    def to_string(self):
        values = []
        current = self.head
        while current:
            print(f'Node val: {current.val}')
            values.append(current.val)
            current = current.next
        return values

    def append(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            return
        last = self.head

        while last.next:
            last = last.next

        last.next = new_node

    def insert_before(self, existing_val, new_val):
        new_node = Node(new_val)
        current = self.head
        while current.next != None:
            if current.next.val == existing_val:
                new_node.next = current.next
                current.next = new_node
                return
            else:
                current = current.next

    def insert_after(self, existing_node, val):

        if existing_node is None:
            print("The input node must be in LinkedList.")
            return

        new_node = Node(val)

        new_node.next = existing_node.next

        existing_node.next = new_node


