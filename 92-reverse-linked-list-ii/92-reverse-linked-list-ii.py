# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        def reverse(move):
            nonlocal head
            prev,cur = None,move
            i = 0
            
            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
                if i == 0:
                    prev.next = head
                i += 1
                
            return prev
        
        to_rev_ptr = ListNode()
        to_rev = to_rev_ptr
        dummy = ListNode()
        cur = ListNode()
        prev = ListNode()
        prev.next = head
        cur = prev
        
        index = 1
        while head:
            if left <= index <= right:
                to_rev.next = head
                to_rev = to_rev.next
                #head.next = reverse(head)
            head = head.next
            if index == right:
                break
            index += 1
            
        to_rev.next = None
        to_rev_ptr = reverse(to_rev_ptr.next)
        
        for _ in range(left-1):
            cur = cur.next

        cur.next = to_rev_ptr
        dummy.next = prev.next
        return dummy.next