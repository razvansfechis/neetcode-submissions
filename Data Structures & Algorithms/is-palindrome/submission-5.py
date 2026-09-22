class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s) - 1

        while i < j:
            while i < j and not s[i].isalpha() and not s[i].isdigit():
                i += 1
            while i < j and not s[j].isalpha() and not s[j].isdigit():
                j -= 1

            is_lower_case_letter = lambda x: 'a' <= x <= 'z'
            is_upper_case_letter = lambda x: 'A' <= x <= 'Z'
            transform_to_lower_case = lambda x: chr(ord(x) - ord('A') + ord('a'))

            left_val = s[i]
            right_val = s[j]

            if left_val.isalpha() and is_upper_case_letter(left_val):
                left_val = transform_to_lower_case(left_val)

            if right_val.isalpha() and is_upper_case_letter(right_val):
                right_val = transform_to_lower_case(right_val)

            if left_val != right_val:
                return False

            i += 1
            j -= 1

        return True