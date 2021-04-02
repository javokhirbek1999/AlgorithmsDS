from LinkedList import LinkedList

def sumLinkedList(ListNode1,ListNode2):
    l1 = ListNode1.head
    l2 = ListNode2.head

    ll = LinkedList()
    t = 0
    while l1 or l2:
        result = t
        if l1:
            result += l1.value
            l1 = l1.next
        if l2:
            result += l2.value
            l2 = l2.next
        ll.add(result%10)
        t = result//10
    return ll
