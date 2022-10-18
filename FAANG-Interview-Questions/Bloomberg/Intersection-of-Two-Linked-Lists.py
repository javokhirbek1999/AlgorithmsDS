"""
Time: O(n)
Space: O(1)
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        lengthA = self.getLength(headA)
        lengthB = self.getLength(headB)
        
        for _ in range(abs(lengthA-lengthB)):
            if lengthA > lengthB:
                headA = headA.next
            else:
                headB = headB.next
            
            
        while headA is not headB:
            headA = headA.next
            headB = headB.next
        
        return headA
        
    
    def getLength(self, head):
        
        size = 0
        
        curr = head
        
        while curr:
            size += 1
            curr = curr.next
        
        return size
