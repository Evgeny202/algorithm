class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        number = [1] * (n + 2)
        for i in range(2, n + 1):
            number[i] = number[i // 2] + number[(i // 2) + 1] * (i % 2)
        return max(number)  #возврат максимального значения nums