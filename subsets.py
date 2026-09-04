class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, nums, curr):
            if i == len(nums):
                res.append(curr.copy())
                return

            # CHOOSE: include nums[i]
            curr.append(nums[i])
            backtrack(i + 1, nums, curr)
            # UNDO: exclude nums[i]
            curr.pop()
            # EXPLORE: skip nums[i]
            backtrack(i + 1, nums, curr)

        backtrack(0, nums, [])
        return res
