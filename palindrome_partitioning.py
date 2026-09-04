class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(start, end):
            """Check if substring s[start:end+1] is a palindrome"""
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
                    current_path.append(s[start:end+1])
                    backtrack(end + 1, current_path)
                    current_path.pop()
        
        result = []
        backtrack(0, [])
        return result