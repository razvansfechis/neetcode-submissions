class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, cur = None, head

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        return prev