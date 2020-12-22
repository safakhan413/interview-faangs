""" Python program to reverse sublist """

# Linked List Node
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Create & Handle List operations
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to display the list
    def printList(self):
        temp = self.head
        # while temp:
        #     print(temp.data)
        #     print(temp.data, end=" ")
        #     temp = temp.next
        while temp is not None:
            print (temp.data)
            temp = temp.next


    # Method to add element to list
    def addToList(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = newNode # append at the end

    #insert new_node after node
    def insert_after(self, node, new_node):
        new_node.next = node.next
        node.next = new_node

    def search_list(L, key):
        while L and L.data != key:
            L = L.next
        # If key was not present in the List, L will become null
        return L

    # Delete the node past this one. Assume node is not a tail
    def delete_after(node):
        node.next = node.next.next

# l1 = LinkedList()
# # print('l1 hey', l1)
# n= [11,3,5,7,2]
# n = Node(11)
# l1.addToList(n)
# # for i in range(0,len(n)-1):
# #     temp = n[i]
# #     n[i] = linked_list.Node(temp)
# #     l1.addToList(n[i])
# l1.printList()