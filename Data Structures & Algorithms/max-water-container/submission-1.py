class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # Create a getArea lambda function
        getArea = lambda lf, rt: (rt - lf) * min(heights[lf], heights[rt])

        # Create 2 pointers
        i, j = 0, len(heights) - 1

        maxArea = 0

        while i < j:
            if getArea(i, j) > maxArea: maxArea = getArea(i, j)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return maxArea