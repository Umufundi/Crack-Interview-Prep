# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:
'''
class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        
        
        
        
        if target != mountain_arr:
            return -1
        
        for i in range(mountain_arr): 
            if mountain_arr[i] != target:
                i+=1
            else:
                if index_found > mountain_arr[i]
                index_found = mountain_arr[i]
                
        return index_found
    
    '''

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # Save the length of the mountain array
        length = mountain_arr.length()

        # 1. Find the index of the peak element
        low = 1
        high = length - 2
        while low != high:
            test_index = (low + high) >> 1
            curr = mountain_arr.get(test_index) 
            next = mountain_arr.get(test_index + 1)
            
            if curr < next:
                if curr == target:
                    return test_index
                if next == target:
                    return test_index + 1
                low = test_index + 1
            else:
                high = test_index
        
        peak_index = low

        # 2. Search in the strictly increasing part of the array
        # If found, will be returned in the loop itself.
        low = 0
        high = peak_index
        while low <= high:
            test_index = (low + high) >> 1
            curr = mountain_arr.get(test_index)
                
            if curr == target:
                return test_index
            elif curr < target:
                low = test_index + 1
            else:
                high = test_index - 1
        
        # 3. Search in the strictly decreasing part of the array
        # If found, will be returned in the loop itself.
        low = peak_index + 1
        high = length - 1
        while low <= high:
            test_index = (low + high) >> 1
            curr = mountain_arr.get(test_index)
                
            if curr == target:
                return test_index
            elif curr > target:
                low = test_index + 1
            else:
                high = test_index - 1
        
        # Target is not present in the mountain array
        return -1    
    
    
    
