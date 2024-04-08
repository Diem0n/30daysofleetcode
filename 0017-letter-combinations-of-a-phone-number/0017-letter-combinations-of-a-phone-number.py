class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        combos = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
        }

        result = ['']

        for digit in digits:
            letters = combos[digit]
            result = [prev_comb + letter for prev_comb in result for letter in letters]

        return result
