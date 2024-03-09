class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        ind = -1  # Step 1: Find the break point:
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                ind = i # index i is the break point
                break
        if ind == -1: # If break point does not exist:
            nums[:] = nums[-1: : -1] # reverse the whole array
            return
        # Step 2: Find the next greater element and swap it with nums[ind]
        for i in range(n-1, ind - 1, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break
        nums[ind+1:]= nums[n-1:ind:-1]  # Step 3: reverse the right half