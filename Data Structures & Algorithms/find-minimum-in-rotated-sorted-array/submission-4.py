class Solution:
    def findMin(self, nums: List[int]) -> int:
        lf, rt = 0, len(nums) - 1

        while lf < rt:
            mid = lf + (rt - lf) // 2

            if nums[mid] > nums[rt]:
                lf = mid + 1
            else:
                rt = mid

        return nums[lf]