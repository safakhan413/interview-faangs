class Node:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next
class SLinkedList:
    def __init__(self):
        self.headVal = None
    #insert new_node after node
    def insert_after(self, node,new_node):
        new_node.next = node.next # new node has old node's next as next
        node.next = new_node # old node's next will be new node

l1 = SLinkedList()
l1Vals = [2,5,7]
l2Vals = [3,11]
l1.headVal = (Node(l1Vals[i]) for i in range(0,len(l1Vals)))
l1.headVal.next =
