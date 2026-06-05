class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst_dict = {}

        for i, e in enumerate(nums):
            lst_dict[e] = i

        for i in range(len(nums)):
            ind = lst_dict.get(target - nums[i])
            if ind is not None and ind != i:
                return [i, ind]
        return []       