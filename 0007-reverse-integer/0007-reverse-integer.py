class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2**31 - 1
        min_int = -2**31

        str_x = str(abs(x))

        reversed_str = str_x[::-1]

        reversed_x = int(reversed_str)

        if x < 0:
            reversed_x *= -1

        if reversed_x > max_int or reversed_x < min_int:
            return 0

        return reversed_x