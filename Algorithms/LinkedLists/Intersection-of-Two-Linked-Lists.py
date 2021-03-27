def intersection(ListNode1,ListNode2):
    if ListNode1.tail is ListNode2.tail:
        return False

    len1 = len(ListNode1)
    len2 = len(ListNode2)

    shorter = ListNode1 if len1<len2 else ListNode2
    longer = ListNode2 if len1<len2 else ListNode1

    diff = len(longer)-len(shorter)

    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next

    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next

    return longerNode   
