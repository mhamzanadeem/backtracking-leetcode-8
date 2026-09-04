class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(current_permutation):
            if len(current_permutation) == len(nums):
                result.append(current_permutation[:])
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    current_permutation.append(nums[i])
                    backtrack(current_permutation)
                    current_permutation.pop()
                    used[i] = False
        
        result = []
        used = [False] * len(nums)
        backtrack([])
        return result