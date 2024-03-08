class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        best_length = 0
        current_length = 0
        for right in range(len(s)):
            if s[right] in seen:
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                    current_length -= 1
                left += 1
            else:
                current_length += 1
                seen.add(s[right])

            if best_length < current_length:
                best_length = current_length

        return best_length