class Solution:
    def trap(self, height: List[int]) -> int:
        left_pointer, right_pointer = 0, len(height) - 1

        max_left = height[0]
        max_right = height[-1]

        res = 0

        while left_pointer < right_pointer:
            if max_left < max_right:
                left_pointer += 1
                max_left = max(max_left, height[left_pointer])
                res += max_left - height[left_pointer]
            else:
                right_pointer -= 1
                max_right = max(max_right, height[right_pointer])
                res += max_right - height[right_pointer]
        return res