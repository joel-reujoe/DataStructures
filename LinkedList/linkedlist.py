class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp=temp.next

    def addNodeAtFront(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head  = new_node
        
    def insertAfter(self, prev_node, data):
        if prev_node == None:
            print("The given node must be in a linked list")
            return
        
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def addNodeAtEnd(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third  = Node(3)
    llist.head.next = second
    second.next = third
    llist.addNodeAtFront(5)
    llist.insertAfter(llist.head, 6)
    llist.addNodeAtEnd(3)
    llist.printList()
