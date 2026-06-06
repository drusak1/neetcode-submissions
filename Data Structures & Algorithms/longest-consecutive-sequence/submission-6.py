class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        longest_len = 1
        sorted_nums = sorted(nums)
        curr_len = 1

        for i in range(1,len(sorted_nums)):
            if (sorted_nums[i] - sorted_nums[i-1]) == 1:
                curr_len += 1
            elif sorted_nums[i] == sorted_nums[i-1]:
                pass
            else:
                curr_len = 1
            longest_len = max(curr_len, longest_len)
        return longest_len
            

            