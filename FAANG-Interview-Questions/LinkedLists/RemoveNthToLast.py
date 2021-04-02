from LinkedList import LinkedList

def removeNthFromEnd(ListNode, n):
        if ListNode is None:
            return None
        
        pointer1 = ListNode.head
        pointer2 = ListNode.head
        
        if pointer1.next is None:
            ListNode.head = None
            return ListNode

        for i in range(n):
            pointer2 = pointer2.next

        if pointer2 is None and n == 2:
            ListNode.head = ListNode.head.next
            return ListNode      


        if pointer2.next is None and n == 1:
            pointer1.next = None
            return pointer1
         

        while pointer2.next:         
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        
        pointer1.next = pointer2
        
        return ListNode.head
