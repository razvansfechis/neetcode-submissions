
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        new_node = head
        if head.next:
            new_node = self.reverseList(head.next)
            head.next.next = head

        head.next = None
        return new_node