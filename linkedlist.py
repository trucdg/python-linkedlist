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

    def delete(self, val):
        """ 
        delete the first node seen with the given value
        """

        # if the list is empty
        if self.head == None:
            print("Deletion Error: the list is empty.")
            return

        # if the head is to be deleted
        if self.head.value == val:
            self.head = self.head.next
        else:
            prev = self.head
            curr = self.head.next

            while (curr and curr.value != val):
                prev = curr
                curr = curr.next
            
            if curr:
                prev.next = curr.next
            else:
                print("Deletion Error: no node with given data found.")

