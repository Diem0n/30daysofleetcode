class Solution:
    def reverseBits(self, n: int) -> int:
        num = format(n , '032b')
        return int(num[::-1],2)