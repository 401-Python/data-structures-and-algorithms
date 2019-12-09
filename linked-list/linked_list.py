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


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
ll = LinkedList()
ll.insert(node1)
ll.insert(node2)
ll.insert(node3)

print(ll.head)
print(ll.to_string())
