class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        visited = set()
        for num in nums:
            if num in visited:
                continue

            curr_num = num
            curr_len = 0
            while curr_num in nums_set:
                curr_len += 1
                visited.add(curr_num)
                curr_num += 1

            max_len = max(max_len, curr_len)
        return max_len