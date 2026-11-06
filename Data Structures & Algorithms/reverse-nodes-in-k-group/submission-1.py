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
        prev_group_end = dummy

        while True:
            curr = prev_group_end.next
            count = 0
            #keep count and make sure it has atleast k elements
            while curr and count < k:
                curr = curr.next
                count += 1
            if count < k:
                break
            
            prev = None
            curr = prev_group_end.next
            tail = curr #this becomes the tail of the reversed group

            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            prev_group_end.next = prev
            tail.next = curr
            prev_group_end = tail
        
        return dummy.next