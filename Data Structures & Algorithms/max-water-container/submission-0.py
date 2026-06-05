class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_pointer, right_pointer = 0, len(heights) - 1
        max_height = 0
        while left_pointer < right_pointer:
            max_height = max(max_height, \
                            min(heights[left_pointer], heights[right_pointer]) \
                            * (right_pointer - left_pointer))
            if heights[left_pointer] < heights[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_height

