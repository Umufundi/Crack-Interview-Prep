from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = deque()

        for i in range(len(nums)):
            # Remove elements that are out of the current window
            while window and window[0] < i - k + 1:
                window.popleft()

            # Remove elements smaller than the current element from the back
            while window and nums[window[-1]] < nums[i]:
                window.pop()

            window.append(i)

            # Add the maximum of the current window to the result
            if i >= k - 1:
                result.append(nums[window[0]])

        return result
