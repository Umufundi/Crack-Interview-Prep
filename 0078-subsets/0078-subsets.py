class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]

        for num in nums:
            temp = []

            for sub in res:
                copy = sub[:]
                copy.append(num)
                temp.append(copy)

            
            res.extend(temp)
        
        return res