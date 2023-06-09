class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def append(self, new_node):
        """ 
        append the new node to the end of the linked list
        """
        # if the llist is empty
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while (curr.next):
                curr = curr.next
            curr.next = new_node

