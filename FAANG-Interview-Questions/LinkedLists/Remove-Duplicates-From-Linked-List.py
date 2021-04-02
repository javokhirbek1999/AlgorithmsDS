from LinkedList import LinkedList

# Time  O(n)
# Space O(n)
# More time efficient
def removeDuplicates(ListNode):
    if ListNode.head is None:
        return None

    current = ListNode.head
    visited_nodes = set([current.value])
    while current.next:
        if current.next.value in visited_nodes:
            current.next = current.next.next
        else:
            visited_nodes.add(current.value)
            current = current.next
    return ListNode.head     

# Time   O(n^2)
# Space  O(1)   
# More space efficient
def removeDuplicates2(ListNode):
    if ListNode.head is None:
        return None

    current = ListNode.head
    while current:
        runner = current
        while runner.next:
            if current.value == runner.next.value:
                runner.next = runner.next.next
            else:
                runner = runner.next 
        current = current.next
    return ListNode.head    
