class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = dict()

        for ind in range(len(nums)):
            second_ind = num_dict.get(target - nums[ind])
            if second_ind is not None:
                return [second_ind, ind]
            num_dict[nums[ind]] = ind
        return []