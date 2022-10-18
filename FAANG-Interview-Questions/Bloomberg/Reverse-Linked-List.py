"""
Time: O(n)
Space: O(1)
"""
# Iterative
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head


        prev = None
        curr = head

        while curr:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next

        return prev
      

"""
Time: O(n)
Space: O(n)
"""
# Recursive
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        
        ll = self.reverseList(head.next)
        
        head.next.next = head
        head.next = None
        
        return ll
