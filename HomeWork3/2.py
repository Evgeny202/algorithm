class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = ''
        pop = head
        while pop:
            num += str(pop.val)
            pop = pop.next
        return(int(num,2))