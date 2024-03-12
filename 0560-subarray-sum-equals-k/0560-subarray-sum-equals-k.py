class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Dictionary to store cumulative sums and their counts
        d = {0: 1}
        sums = 0  # Cumulative sum
        count = 0  # Result counter

        # Iterate through the array
        for i in range(len(nums)):
            sums += nums[i]  # Update cumulative sum

            # If (current cumulative sum - k) exists in the dictionary, add its count to the result
            if sums - k in d:
                count += d[sums - k]

            # Update the dictionary with the current cumulative sum
            if sums in d:
                d[sums] += 1
            else:
                d[sums] = 1

        return count