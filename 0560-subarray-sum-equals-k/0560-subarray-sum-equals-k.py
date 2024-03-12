class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {0: 1}

        prefix_sum = 0
        ans = 0 
        for n in nums:
            prefix_sum += n
            if prefix_sum - k in prefix_map:
                ans += prefix_map[prefix_sum - k]
            
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

        return ans