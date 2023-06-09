class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def append(self, new_value):
        """ 
        append the new value to the end of the linked list
        """
        new_node = Node(new_value)

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

    def print(self):
        current = self.head
        s = ""

        while current:
            s += str(current.value) + "->"
            current = current.next
        
        s += "None"

        print(s)

if __name__ == "__main__":
    # create a linked list
    ll = LinkedList()
    ll.append(6)
    ll.append(7)
    ll.append(8)
    ll.append(6)

    ll.print()


