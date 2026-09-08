class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""
        for val in strs:
            final_str += str(len(val)) + '#' + val

        return final_str

    def decode(self, s: str) -> List[str]:
        lst, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            lst.append(s[j + 1: j + 1 + length])
            i = j + 1 + length

        return lst