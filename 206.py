from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        newh = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None

        return newh
    
    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            temp = curr.next
            head.next = prev
            prev = head
            curr = temp

        return prev
    
    # Space Complexity: O(1)
    # Time Complexity: O(n) 