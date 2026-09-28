class Solution:
    def binarySearch(self, nums, target, lf, rt):

        mid = lf + (rt - lf) // 2

        if lf <= rt:
            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                return self.binarySearch(nums, target, mid + 1, rt)
            else:
                return self.binarySearch(nums, target, lf, mid - 1)

        else:
            return -1

    def search(self, nums: List[int], target: int) -> int:

        lf, rt = 0, len(nums) - 1

        while lf < rt:
            mid = lf + (rt - lf) // 2

            if nums[mid] > nums[rt]:
                lf = mid + 1
            else:
                rt = mid

        next_array_start = lf

        lf_array_lf = 0
        lf_array_rt = next_array_start - 1

        rt_array_lf = next_array_start
        rt_array_rt = len(nums) - 1

        pos = self.binarySearch(nums, target, lf_array_lf, lf_array_rt)
        if pos == -1:
            pos = self.binarySearch(nums, target, rt_array_lf, rt_array_rt)

        return pos