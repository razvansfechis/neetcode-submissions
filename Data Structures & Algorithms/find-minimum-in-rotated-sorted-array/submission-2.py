class Solution:
    def binarySearch(self, nums, lf, rt):

        mid = (lf + rt) // 2

        if lf == rt:
            if len(nums) == 1 or nums[lf + 1] > nums[0]:
                return nums[0]

            return nums[lf + 1]

        if nums[mid] > nums[lf]:
            return self.binarySearch(nums, mid, rt)
        else:
            return self.binarySearch(nums, lf, mid)


    def findMin(self, nums: List[int]) -> int:

        x = self.binarySearch(nums, 0, len(nums) - 1)

        return x