class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}
        
        for i in range(len(nums)):
            indexMap[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in indexMap and indexMap[diff] != i:
                return [i, indexMap[diff]]