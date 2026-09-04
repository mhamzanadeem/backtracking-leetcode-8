class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def backtrack(start, current_path):
            if start == len(s):
                result.append(current_path[:])
                return

            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    # CHOOSE: take substring as partition
                    current_path.append(s[start:end + 1])
                    backtrack(end + 1, current_path)
                    # UNDO
                    current_path.pop()
                    # EXPLORE: loop tries next end position

        result = []
        backtrack(0, [])
        return result
