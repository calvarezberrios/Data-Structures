"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

import os
import sys

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from linked_list import LinkedList
from stack.stack import Stack
class Queue:
    def __init__(self, storage = LinkedList()):
        self.size = 0
        self.storage = storage

    def __str__(self):
        if isinstance(self.storage, list) == True:
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

    def enqueue(self, value):
        if isinstance(self.storage, LinkedList) == False:
            self.storage.insert(0, value)
        else:
            self.storage.add_to_head(value)
            self.size += 1

    def dequeue(self):
        if isinstance(self.storage, LinkedList) == False:
            if self.size > 0:
                return self.storage.pop()
        else:
            if self.size > 0:
                dequeued = self.storage.remove_tail()
                self.size -= 1
                return dequeued



# arrQ = Queue()
# print("Starting length Array Queue: ", len(arrQ))

# print(arrQ)

# arrQ.enqueue(75)
# print("Array Queue Length after enqueue: ", len(arrQ))

# print(arrQ)

# arrQ.enqueue(4)
# print("Array Queue Length after enqueue: ", len(arrQ))

# print(arrQ)

# arrQ.enqueue(21)
# print("Array Queue Length after enqueue: ", len(arrQ))

# print(arrQ)

# arrQ.enqueue(5)
# print("Array Queue Length after enqueue: ", len(arrQ))

# print(arrQ)


# removed = arrQ.dequeue()
# print(f"Array length after dequeue: {len(arrQ)}, removed: {removed}")

# print(arrQ)