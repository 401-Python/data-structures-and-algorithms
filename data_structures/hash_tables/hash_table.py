from hashlib import md5
# from linked_list.linked_list import LinkedList



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

defaultHashTableSize = 32

class HashTable:

    def __init__(self, hashTableSize = defaultHashTableSize):
        
        self.buckets = [LinkedList() for x in range(0, hashTableSize)]

        self.keys = {}


    def add(self, key, value):

        key_index = self.hash(key)
        self.keys[key] = key_index
        
        # refers to a Linked List in the bucket array, at the key index
        bucket = self.buckets[key_index]  
        
        node = bucket.find({key: value})
        
        if node == None: # the key doesn't exist
            bucket.append({key: value})
        else: # key already exists, add new value
            node.value.value = value

  
    def get(self, key):

        bucket = self.buckets[self.hash(key)]

        currentNode = bucket.head
        while not currentNode == None:
            for k in currentNode.value:
                if k == key:
                    return currentNode.value[k]
            currentNode = currentNode.next

        print('key not found')
        return None
    
  
    def hash(self, key):
        k = 0
        # found via stack overflow, this converts the key to a string encoded to utf-8
        # converts the string to a list of seperated vals
        # loop through and convert each character into its code point integer
        # and accumulate those values with k
        for char in list(md5(str(key).encode('utf-8')).hexdigest()):
            # ord returns an integer representing the unicode code point
            k += ord(char)
            # mod by the length of bucket list to obain hashed key
        return k % len(self.buckets)

 
    def contains(self, key):
        if key in self.keys.keys():
            print('key present')
            return True
        else:
            print('key not found')
            return False

if __name__ == "__main__":
    ht = HashTable()
    ht.add('testing', 72)
    ht.contains('fart')