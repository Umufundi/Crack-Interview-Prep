class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Step 1: Create a set 'num' to efficiently check the presence of numbers.
        num = set(nums)
        longest = 0

        # Step 2: Iterate through each number in 'nums'.
        for x in nums:
            # If 'x-1' is not in 'num', it means 'x' is potentially the start of a consecutive sequence.
            if x - 1 not in num:
                l = 0
                # Step 3: While (x + l) is in 'num', count the length of the consecutive sequence.
                while (x + l) in num:
                    l += 1
                # Update 'longest' if the current sequence length is greater.
                longest = max(l, longest)

        # Step 4: Return the length of the longest consecutive sequence.
        return longest