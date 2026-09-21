class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)

        biggest_seq_len = 0

        for el in nums_set:

            curr_seq_len = 1

            if el - 1 not in nums_set:
                starting_val = el

                next_val = starting_val + 1

                while next_val in nums_set:
                    curr_seq_len += 1
                    next_val += 1

                if curr_seq_len > biggest_seq_len:
                    biggest_seq_len = curr_seq_len

        return biggest_seq_len