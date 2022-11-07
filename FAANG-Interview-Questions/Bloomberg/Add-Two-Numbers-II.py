"""
Time: O(N)
Space: O(N)
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1 = self.reverseLL(l1)
        l2 = self.reverseLL(l2)
        
        
        dummy = ListNode(0)
        tail = dummy
        
        
        carry = 0
        
        while l1 or l2:
            temp = carry
            if l1:
                temp += l1.val
                l1 = l1.next
            
            if l2:
                temp += l2.val
                l2 = l2.next
            
            tail.next = ListNode(temp%10)
            tail = tail.next
            
            carry = temp//10
        
        
        if carry != 0:
            tail.next = ListNode(carry)
            tail = tail.next
        
        dummy = self.reverseLL(dummy.next)
        
        return dummy
        
    
    def reverseLL(self, LL):
        
        prev = None
        current = LL
        
        while current:
            _next = current.next
            current.next = prev
            prev = current
            current = _next
        
        LL = prev
        
        return LL
