## Code ref https://stackabuse.com/doubly-linked-list-with-python-examples/

class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None
class DLinkedList:
    def __init__(self):
        self.headVal = None

    ## inserting data
    def insert_in_emptylist(self, data):
        if self.headVal is None:
            new_node = Node(data)
            self.headVal = new_node
        else:
            print("list is not empty")

    def insert_at_start(self, data):
        if self.headVal is None:
            new_node = Node(data)
            self.headVal = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.next = self.headVal
        self.headVal.prev = new_node
        self.headVal = new_node
    def insert_after_item(self, x, data):
        if self.headVal is None:
            print("List is empty")
            return
        else:
            n = self.headVal
            while n is not None:
                if n.item == x:
                    break
                n = n.next
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.prev = n
                new_node.next = n.next
                if n.next is not None:
                    n.next.prev = new_node
                n.next = new_node

    def insert_before_item(self, x, data):
        if self.headVal is None:
            print("List is empty")
            return
        else:
            n = self.headVal
            while n is not None:
                if n.item == x:
                    break
                n = n.next
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.next = n
                new_node.prev = n.prev
                if n.prev is not None:
                    n.prev.next = new_node
                n.prev = new_node

    def traverse_list(self):
        if self.headVal is None:
            print("List has no element")
            return
        else:
            n = self.headVal
            while n is not None:
                print(n.item, " ")
                n = n.nref