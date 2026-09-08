class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_list = []
        sufix_list = []

        # Initialize the lists
        for num in nums:
            prefix_list.append(1)
            sufix_list.append(1)

        # Create prefix list
        for idx in range(1, len(nums)):
            prefix_list[idx] = prefix_list[idx - 1] * nums[idx-1]

        for idx in range(len(nums)-2, -1, -1):
            sufix_list[idx] = sufix_list[idx+1] * nums[idx+1]

        final_list = []

        for num in nums:
            final_list.append(None)

        for idx in range(len(prefix_list)):
            final_list[idx] = prefix_list[idx] * sufix_list[idx]

        return final_list