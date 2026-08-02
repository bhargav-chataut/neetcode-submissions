from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp_hash = defaultdict(int)
        out = []
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in comp_hash:
                out.append(comp_hash[complement])
                out.append(i)

            comp_hash[nums[i]] = i
            
        return out