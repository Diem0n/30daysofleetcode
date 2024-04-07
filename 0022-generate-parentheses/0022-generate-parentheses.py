class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(curr_str, open_count, close_count):
            if len(curr_str) == 2 * n:
                result.append(curr_str)
                return
            if open_count < n:
                backtrack(curr_str + "(", open_count + 1, close_count)
            if close_count < open_count:
                backtrack(curr_str + ")", open_count, close_count + 1)

        result = []
        backtrack("", 0, 0)
        return result