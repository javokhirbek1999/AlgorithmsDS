"""
Time: O(n)
Space: O(1)
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:  
        
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            
            if list1.val < list2.val:
                tail.next = list1
                tail = tail.next
                list1 = list1.next
            else:
                tail.next = list2
                tail = tail.next
                list2 = list2.next
        
        if list1:
            tail.next = list1
        
        if list2:
            tail.next = list2
        
        return dummy.next
        
