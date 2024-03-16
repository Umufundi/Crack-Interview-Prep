class Solution:
    def rob(self, nums: List[int]) -> int:
        h1 , h2 = 0 , 0
        #nums = [house1, house2, n, n+1]
        for n in nums:
            tmp = max(h1+n, h2)
            h1 = h2
            h2 = tmp
        return h2
        # sum1 = sum2 = 0
        # for i in range(0, len(nums), 2):
        #     sum1+= nums[i]
        # for j in range(1, len(nums), 2):
        #     sum2+= nums[j]
        # return sum1 if sum1> sum2 else sum2