

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

    def merge(self, linkedlist_):
        current_a = self.head
        current_b = linkedlist_.head

        # While there are available positions in p;
        while current_a and current_b:

            # Save next pointers
            a_next = current_a.next
            b_next = current_b.next

            # make q_curr as next of p_curr
            current_b.next = a_next  # change next pointer of q_curr
            current_a.next = current_b  # change next pointer of p_curr

            # update current pointers for next iteration
            current_a = a_next
            current_b = b_next
        linkedlist_.head = current_b


ll = LinkedList()
ll.insert(1)
ll.append(3)
ll.append(5)
ll.append(7)

ll2 = LinkedList()
ll.insert(2)
ll.append(4)
ll.append(6)
ll.append(8)

ll.merge(ll2)
ll.__str__()
