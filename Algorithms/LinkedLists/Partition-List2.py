def partition(ListNode,x):
    if ListNode.head is None:
        return None

    current = ListNode.head
    ListNode.tail = ListNode.head
    
    while current:
        next_node = current.next
        current.next = None
        if current.value < x:
            current.next = ListNode.head
            ListNode.head = current
        else:
            ListNode.tail.next = current
            ListNode.tail = current
        current = next_node
       
    if ListNode.tail.next is not None:
        ListNode.tail.next = None
    return ListNode
