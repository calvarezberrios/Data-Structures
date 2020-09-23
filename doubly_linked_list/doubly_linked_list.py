"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node

    def get_prev(self):
        return self.prev

    def set_prev(self, node):
        self.prev = node



            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.set_prev(new_node)
            new_node.set_next(self.head)
            self.head = new_node
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        value = self.head.get_value()
        self.delete(self.head)
        return value


            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            new_node.set_prev(self.tail)
            self.tail = new_node
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.get_value()
        self.delete(self.tail)
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.get_value())
            
        

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.get_value())

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # Get the prev and next of the input node
        prevNode = node.get_prev()
        nextNode = node.get_next()

        if not self.head and not self.tail:
            return

        if self.head == self.tail and node == self.head:
            self.head = None
            self.tail = None
        elif self.length == 2:
            if self.head == node:
                self.head = self.tail
            elif self.tail == node:
                self.tail = self.head
        else:
            if prevNode:
                prevNode.set_next(nextNode)
            if nextNode:
                nextNode.set_prev(prevNode)
        self.length -= 1
            
            
            

            


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current_node = self.head

        if self.length == 0:
            return 0
        
        maxValue = current_node.get_value()

        while current_node.get_next():
            if maxValue < current_node.get_next().get_value():
                maxValue = current_node.get_next().get_value()
                current_node = self.head
            else:
                current_node = current_node.get_next()

        return maxValue