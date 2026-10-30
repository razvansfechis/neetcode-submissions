class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        total_subarrays = 0
        sum = 0
        prefixSum = defaultdict(int)

        prefixSum[0] = 1

        for val in nums:

            sum += val

            if sum - k in prefixSum:
                total_subarrays += prefixSum[sum - k]

            prefixSum[sum] += 1

        return total_subarrays