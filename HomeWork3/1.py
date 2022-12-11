class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        num = []
        p = head
        while p.next:
            num.append(p.val)
            p = p.next
        num.append(p.val)
        return num == num[::-1]