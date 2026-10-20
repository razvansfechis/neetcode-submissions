class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos_set = defaultdict(int)
        lf = 0
        max_subs_len = 0

        for rt in range(len(s)):
            if s[rt] in pos_set:
                lf = max(lf, pos_set[s[rt]] + 1)

            pos_set[s[rt]] = rt

            max_subs_len = max(max_subs_len, rt - lf + 1)

        return max_subs_len