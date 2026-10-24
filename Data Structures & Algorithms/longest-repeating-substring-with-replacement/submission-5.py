class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = defaultdict(int)

        lf = 0
        longest_subs = 0

        rt = 0

        most_freq_char = None
        most_freq_len = 0

        while rt <= len(s) - 1 and lf <= len(s) - 1:

            char_freq[s[rt]] += 1

            for ch in char_freq:
                if char_freq[ch] > most_freq_len:
                    most_freq_len = char_freq[ch]
                    most_freq_char = ch

            if rt - lf + 1 - most_freq_len > k:
                char_freq[s[lf]] -= 1
                lf += 1

            if rt - lf + 1 - most_freq_len <= k:
                longest_subs = max(longest_subs, rt - lf + 1)
                rt += 1

        return longest_subs