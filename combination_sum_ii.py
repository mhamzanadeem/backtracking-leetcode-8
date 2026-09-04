class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, remaining, current_combination):
            if remaining == 0:
                result.append(current_combination[:])
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining:
                    break

                # CHOOSE
                current_combination.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i], current_combination)
                # UNDO
                current_combination.pop()
                # EXPLORE: loop continues to next i

        candidates.sort()
        result = []
        backtrack(0, target, [])
        return result
