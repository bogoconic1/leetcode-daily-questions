# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        def reverse(move):
            prev,cur = None,move
            
            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
                
            return prev
        
        def merge(a,b,c):
            dummy = tail = ListNode()
            while a:
                tail.next = a
                tail = tail.next
                a = a.next
            while b:
                tail.next = b
                tail = tail.next
                b = b.next
            while c:
                tail.next = c
                tail = tail.next
                c = c.next
            
            tail.next = None
            return dummy.next
        
        def split(head,threshold):
            if threshold == 1:
                return None,head
            slow = ListNode(-1000)
            slow.next = head
            index = 1
            while index < threshold:
                slow = slow.next
                index += 1
            secondhead = slow.next
            slow.next = None
            return head,secondhead

        a,b = split(head,left)
        b,c = split(b,right-left+2)
        b = reverse(b)
        #return b
        return merge(a,b,c)