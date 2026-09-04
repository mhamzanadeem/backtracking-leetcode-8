class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return

            if i >= len(candidates) or total > target:
                return

            # CHOOSE: include candidates[i] (can reuse)
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            # UNDO
            curr.pop()
            # EXPLORE: skip to next candidate
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res
