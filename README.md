# Backtracking - LeetCode 8

Solutions for LeetCode backtracking problems.

## Generic Backtracking Skeleton

```python
def backtrack(path, choices):
    if base_case(path):
        result.append(path[:])  # record solution
        return

    for choice in choices:
        # CHOOSE: make a decision
        path.append(choice)

        # EXPLORE: recurse with updated state
        backtrack(path, new_choices)

        # UNDO: revert decision (backtrack)
        path.pop()
```

Every backtracking problem follows this pattern: **choose**, **explore**, **undo**. The differences are in what constitutes a "choice," how you detect the base case, and what pruning/optimizations are applied.

---

## Problems

| # | Problem | File |
|---|---------|------|
| 1 | Subsets | `subsets.py` |
| 2 | Combination Sum | `combination_sum.py` |
| 3 | Combination Sum II | `combination_sum_ii.py` |
| 4 | Permutations | `permutations.py` |
| 5 | Subsets II | `subsets_ii.py` |
| 6 | Palindrome Partitioning | `palindrome_partitioning.py` |
| 7 | Letter Combinations of a Phone Number | `letter_combinations_of_a_phone_number.py` |
| 8 | N-Queens | `n_queens.py` |

---

## How Subsets II Skips Duplicate Branches

**Problem:** Given `nums = [1, 2, 2]`, plain subsets would produce `[1,2,2]` twice because the two `2`s are treated as distinct.

**Solution:** Sort the array first, then when skipping a value, skip ALL duplicates of that value at the same recursion level.

```python
# After choosing nums[i] and undoing it:
idx = i + 1
while idx < len(nums) and nums[idx] == nums[idx - 1]:
    idx += 1          # skip over duplicate values
backtrack(idx, nums, curr)  # jump past all duplicates
```

**Key insight:** Sorting groups duplicates together. The `while` loop skips consecutive equal elements **at the same tree level**, ensuring each unique subset is generated exactly once. We still include the first occurrence (via the choose branch) but skip the rest (via the skip branch).

---

## N-Queens: Column and Diagonal Constraints

The goal is to place N queens on an N×N board so no two attack each other.

**Column constraint:** `cols` set tracks which columns are occupied. A queen at `(row, col)` blocks column `col`.

**Diagonal constraints:** Two types of diagonals exist:

| Diagonal | Formula | Reason |
|----------|---------|--------|
| `\` (top-left to bottom-right) | `row - col` | Constant along this diagonal |
| `/` (top-right to bottom-left) | `row + col` | Constant along this diagonal |

```python
if col in cols or (row - col) in diag1 or (row + col) in diag2:
    continue  # skip this position — conflict
```

**Choose:** Place queen at `(row, col)`, add to `cols`, `diag1`, `diag2`.
**Explore:** Recurse to next row.
**Undo:** Remove queen and update sets.

Since we place one queen per row, we never need to check row conflicts.

---

## How Each Problem Maps to the Skeleton

| Problem | CHOOSE | EXPLORE | UNDO |
|---------|--------|---------|------|
| Subsets | `curr.append(nums[i])` | recurse on `i+1` (include) and `i+1` (exclude) | `curr.pop()` |
| Combination Sum | `curr.append(candidates[i])` | recurse with same `i` (reuse) or `i+1` (skip) | `curr.pop()` |
| Combination Sum II | `curr.append(candidates[i])` | recurse with `i+1` | `curr.pop()` |
| Permutations | `used[i]=True; curr.append(nums[i])` | recurse on all unused | `curr.pop(); used[i]=False` |
| Subsets II | `curr.append(nums[i])` | recurse on `i+1`, skip duplicates on skip | `curr.pop()` |
| Palindrome Partitioning | `path.append(substring)` | recurse from `end+1` | `path.pop()` |
| Letter Combinations | pass new string `curStr + c` | recurse on `i+1` | implicit (new string) |
| N-Queens | `board[row][col]='Q'; add to sets` | recurse on `row+1` | `board[row][col]='.'; remove from sets` |
