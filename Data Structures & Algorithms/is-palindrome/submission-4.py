class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_string = ""

        for val in s:

            small_letter = ('a' <= val <= 'z')
            big_letter = ('A' <= val <= 'Z')

            if small_letter or big_letter:

                if big_letter:
                    clean_string += chr(ord('a') + ord(val) - ord('A'))
                else:
                    clean_string += val

            else:
                try:
                    if 0 <= int(val) <= 9:
                        clean_string += val
                except Exception:
                    continue

        i = 0
        j = len(clean_string) - 1

        while i < j:
            if clean_string[i] != clean_string[j]:
                return False

            i += 1
            j -= 1


        return True