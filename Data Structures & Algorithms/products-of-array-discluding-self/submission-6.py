class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count, prod = 0, 1
        lst = [0] * len(nums)
        for num in nums:
            if num: prod *= num
            else: zero_count += 1

        if zero_count > 1: return lst
        for idx, num in enumerate(nums):
            if zero_count: lst[idx] = (0 if num else prod)
            else: lst[idx] = prod // num

        return lst