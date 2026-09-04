class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, nums, curr):
            if i == len(nums):
                res.append(curr.copy())
                return

            # CHOOSE: include nums[i]
            curr.append(nums[i])
            backtrack(i + 1, nums, curr)
            # UNDO
            curr.pop()
            # EXPLORE: skip duplicates to avoid duplicate subsets
            idx = i + 1
            while idx < len(nums) and nums[idx] == nums[idx - 1]:
                idx += 1
            backtrack(idx, nums, curr)

        backtrack(0, nums, [])
        return res
