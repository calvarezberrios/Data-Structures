"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

import os
import sys

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from linked_list import LinkedList

class Stack:
    def __init__(self, storage = LinkedList()):
        self.size = 0
        self.storage = storage

    def __str__(self):
        if isinstance(self.storage, LinkedList) == False:
            return f"{self.storage}"
        else:
            linkedList = []
            if self.storage.head == None and self.storage.tail == None:
                linkedList = []
            elif self.storage.head == self.storage.tail:
                linkedList.append(self.storage.tail.get_value())
            else:
                current_node = self.storage.head
                while current_node.get_next() != None:
                    linkedList.append(current_node.get_value())
                    current_node = current_node.get_next()
                    if current_node.get_next() == None:
                        linkedList.append(current_node.get_value())

            return f"LinkedList{linkedList}"

    
    def __len__(self):
        if isinstance(self.storage, LinkedList) == False:
            self.size = len(self.storage)

        return self.size

    def push(self, value):
        if isinstance(self.storage, LinkedList) == False:
            self.storage.append(0, value)
        else:
            self.storage.add_to_tail(value)
            self.size += 1

    def pop(self):
        if isinstance(self.storage, LinkedList) == False:
            if self.size > 0:
                return self.storage.pop()
        else:
            if self.size > 0:
                dequeued = self.storage.remove_tail()
                self.size -= 1
                return dequeued


# arrQ = Stack()
# print("Starting length Array Queue: ", len(arrQ))

# print(arrQ)

# arrQ.push(75)
# print("Array Stack Length after enqueue: ", len(arrQ))

# print(arrQ)

# arrQ.push(4)
# print("Array Stack Length after enqueue: ", len(arrQ))

# print(arrQ)

# arrQ.push(21)
# print("Array Stack Length after enqueue: ", len(arrQ))

# print(arrQ)

# arrQ.push(5)
# print("Array Stack Length after enqueue: ", len(arrQ))

# print(arrQ)


# removed = arrQ.pop()
# print(f"Array length after dequeue: {len(arrQ)}, removed: {removed}")

# print(arrQ)