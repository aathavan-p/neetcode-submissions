# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1: return head
        dummy = ListNode
        dummy.next = head

        groupprev = dummy

        while True:
            curr = groupprev.next
            count = 0
            while curr and count < k:
                curr = curr.next
                count += 1
            if count < k:
                break
            
            prev = None
            curr = groupprev.next
            tail = curr

            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            groupprev.next = prev
            tail.next = curr
            groupprev = tail
        
        return dummy.next