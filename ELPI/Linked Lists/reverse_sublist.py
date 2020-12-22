#!/usr/bin/env python3

import linked_list

l1 = linked_list.LinkedList()
l1.head = linked_list.Node(11)
tail = l1.head

n= [3,5,7,2]
for i in range(0,len(n)):
    temp = n[i]
    n[i] = linked_list.Node(temp)
    l1.insert_after(tail,n[i])
    tail = n[i]

def printList(msg, head):
    print(msg, end=': ')
    ptr = head
    while ptr:
        print(ptr.data, end=" -> ")
        ptr = ptr.next
    print("None")


# Iteratively reverse a linked list from position m to n
def reverse(head, m, n):
    prev = None
    curr = head

    # 1. Skip the first m nodes
    i = 1
    while curr is not None and i < m:
        prev = curr
        curr = curr.next
        i = i + 1

    # prev now points to position the (m-1)'th node
    # curr now points to position the m'th node

    start = curr
    end = None

    # 2. Traverse and reverse the sub-list from position m to n
    while curr is not None and i <= n:
        # Take note of the next node
        next = curr.next # e.g.5

        # move the 'curr' node onto the 'end'
        curr.next = end # none
        end = curr #

        # move to the next node
        curr = next
        i = i + 1

    # start points to the m'th node
    # end now points to the n'th node
    # curr now points to the (n+1)'th node

    # 3. Fix the pointers and return the head node
    start.next = curr
    if prev is None:  # when m = 1 (prev is None)
        head = end
    else:
        prev.next = end

    return head

(m, n) = (2, 4)
printList("Original Linked List", l1.head)
head = reverse(l1.head, m, n)
printList("Reversed Linked List", l1.head)

