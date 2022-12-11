class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cat = head
        mouse = head
        while mouse and mouse.next:
            cat = cat.next
            mouse = mouse.next.next
            if cat == mouse:
                return 'true'
            else:
                return 'false'