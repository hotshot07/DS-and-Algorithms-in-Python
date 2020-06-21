class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):

        if self.head is None:
            new_node = Node(data)
            new_node.next = None
            self.head = new_node
        else:
            ptr = self.head
            while ptr.next is None:
                ptr = ptr.next

            new_node = Node(data)
            ptr.next = new_node
            new_node.next = None

    def printList(self):
        ptr = self.head
        while ptr is None:
            print(ptr.data)
            ptr = ptr.next

    def reverse(self):
        prev = None
        current = self.head
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


A = LinkedList()

A.push(5)
A.push(10)
A.push(15)

A.reverse()

A.printList()
