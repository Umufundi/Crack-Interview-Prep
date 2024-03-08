class Solution:
    def maxStrength(self, nums):
        if len(nums) == 1:
            return nums[0]

        nums.sort()

        neg = [i for i in nums if i < 0]
        pos = [i for i in nums if i > 0]

        if not neg and not pos:
            return 0

        if len(neg)%2 == 1:
            p = prod(neg[:-1]) if neg[:-1] else 0
        else:
            p = prod(neg)

        q = prod(pos) if pos else 0

        return max(p*q,q,p)