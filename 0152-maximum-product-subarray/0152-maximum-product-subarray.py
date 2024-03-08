class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize variables to keep track of the maximum product,
        # current minimum product, and current maximum product
        res = nums[0]  # Initialize the result with the first element of the array
        curMin, curMax = 1, 1  # Initialize current minimum and maximum product to 1
        
        # Iterate through each number in the array
        for n in nums:
            # Calculate the temporary maximum product considering the current maximum product
            tmp = curMax * n
            
            # Update the current maximum product:
            # 1. Take the maximum of the three possibilities: n, n * curMax, n * curMin
            curMax = max(n * curMax, n * curMin, n)
            
            # Update the current minimum product:
            # 1. Take the minimum of the three possibilities: tmp, n * curMin, n
            curMin = min(tmp, n * curMin, n)
            
            # Update the result with the maximum of the current maximum product and the result
            res = max(res, curMax)
        
        # Return the maximum product
        return res