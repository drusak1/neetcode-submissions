class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amount = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                max_amount = max(min(heights[i],heights[j]) * (i-j),max_amount)
        return max_amount