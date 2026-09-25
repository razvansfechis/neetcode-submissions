class Solution:
    def isOpposite(self, lf:str, rt:str) -> bool:
        if lf == '[':
            return rt == ']'

        elif lf == '(':
            return rt == ')'

        elif lf == '{':
            return rt == '}'

        return False

    def isValid(self, s: str) -> bool:

        stack = []

        for val in s:

            if not stack:
                stack.append(val)

            elif self.isOpposite(stack[-1], val):
                stack.pop()
            else:
                stack.append(val)

        return stack == []