def has_cycle(head):
    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast: # There is a cycle.
            # Tries to find the start of the cycle.
            slow = head
            # Both pointers advance at the sane time,
            while slow is not fast:
                slow, fast = slow.next, fast.next
                return slow # sTow is the start of cycle
    return None # No cycle.