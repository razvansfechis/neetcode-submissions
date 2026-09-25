class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 == 1: return False

        stack = []

        pairs = defaultdict(str)

        pairs[')'] = '('
        pairs[']'] = '['
        pairs['}'] = '{'

        for val in s:
            if stack and pairs[val] == stack[-1]:
                stack.pop()
            else:
                stack.append(val)

        return not stack