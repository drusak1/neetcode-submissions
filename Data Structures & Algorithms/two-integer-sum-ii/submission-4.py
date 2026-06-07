class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            curr_num = numbers[left] + numbers[right]

            if curr_num == target:
                return [left+1, right+1]

            if curr_num > target:
                right -= 1
            else:
                left += 1
        return [-1,-1]