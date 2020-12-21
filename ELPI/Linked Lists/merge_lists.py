class Node:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next
class SLinkedList:
    def __init__(self):
        self.headVal = None
    #insert new_node after node
    def insert_after(self, node,new_node):
