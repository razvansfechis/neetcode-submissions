class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        total_lsts = []

        for i, left_val in enumerate(nums):
            hash_map = {}

            for j, right_val in enumerate(nums[i+1:], start=i+1):
                searched_val = - left_val - right_val

                if searched_val in hash_map:
                    current_lst = sorted([left_val, right_val, searched_val])
                    if current_lst not in total_lsts:
                        total_lsts.append(current_lst)

                hash_map[right_val] = j


        return total_lsts