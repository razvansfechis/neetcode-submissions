class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        zero_count, prod, lst = 0, 1, []
        for num in nums:

            if num != 0:
                prod *= num

            if num == 0:
                zero_count += 1

        if zero_count > 1:
            return [0] * len(nums)

        elif zero_count == 1:
            idx = 0
            for num in nums:
                if num == 0:
                    lst.append(prod)
                else:
                    lst.append(0)

        else:
            for num in nums:
                lst.append(prod // num)

        return lst