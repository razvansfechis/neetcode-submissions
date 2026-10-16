class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        chr_lst = defaultdict(int)

        longest_seq = 1
        current_seq = 1

        lf = 0
        chr_lst[s[lf]] = 1

        for rt in range(lf + 1, len(s)):
            chr_lst[s[rt]] += 1

            current_seq += 1

            while chr_lst[s[rt]] == 2:
                chr_lst[s[lf]] -= 1
                lf += 1
                current_seq -= 1

            longest_seq = max(longest_seq, current_seq)

        return longest_seq