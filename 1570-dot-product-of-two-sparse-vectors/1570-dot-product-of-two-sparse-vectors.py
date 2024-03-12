class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        # len(vec) == len(self.nums)
        sum = 0
        for i in range(len(vec.nums)):
            sum += self.nums[i] * vec.nums[i]
        return sum