class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None:
            return None
                
        part1, part2 = ListNode(), ListNode()
        tail1, tail2 = part1, part2
        
        while head:
            if head.val < x:
                tail1.next = head
                tail1 = tail1.next
            else:
                tail2.next = head
                tail2 = tail2.next
            head = head.next
        
        tail1.next = part2.next
        tail2.next = None
        
        return part1.next
        
