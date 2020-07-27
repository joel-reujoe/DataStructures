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

    def deleteANode(self, key):
        temp = self.head
        
        if(temp is not None):
            if(temp.data == key):
                self.head = temp.next
                temp = None
                return

        while(temp is not None):
            if(temp.data == key):
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None

    def getLengthRec(self, node):
        if (not node):
            return 0
        else:
            return 1 + self.getLengthRec(node.next)

    def deleteANodeByPosition(self, pos):
        if self.head == None:
            return

        temp = self.head
        if pos == 0:
            self.head = temp.next
            temp = None
            return

        for i in range(pos-1):
            temp = temp.next
            if temp is None:
                break
        
        if temp is None:
            return
        if temp.next is None:
            return

        next = temp.next.next
        temp.next = None
        temp.next = next

    def deleteList(self):
        current = self.head
        while current:
            prev = current.next
            del current.data
            current = prev

    def printLength(self):
        temp = self.head
        count = 0

        while(temp):
            count += 1
            temp = temp.next
        
        print(count)

    def search(self, x):
        temp = self.head
        while(temp):
            if(temp.data==x):
                return True
            temp = temp.next
        
        return False



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
    print("delete")
    llist.deleteANode(3)
    llist.deleteANode(5)
    llist.deleteANode(7)
    llist.deleteANodeByPosition(3)
    llist.deleteANodeByPosition(0)
    llist.printList()
    llist.insertAfter(llist.head,7)
    llist.printList()
    llist.printLength()
    print(llist.getLengthRec(llist.head))
    if(llist.search(7)):
        print("yes")
    else:
        print("no")
