class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        station = 0
        Sum = 0
        
        for i in range(len(gas)):
            Sum += gas[i] - cost[i]
            if Sum < 0:
                Sum = 0
                station = i + 1
        
        return station