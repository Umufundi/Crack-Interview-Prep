class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # add zeros at the ends
        flowerbed=[0]+flowerbed+[0]
        
        #iterate over indexes
        for i in range(1,len(flowerbed)-1):
            
            # check if 3 items in the list are consecutively zero
            if (flowerbed[i]==0 
                and flowerbed[i+1]==0 
                and flowerbed[i-1]==0):
                
                # if so check item at i to 1 and decrement n
                flowerbed[i]=1
                n-=1
        # after the iteration, if n is zero or lower return true        
        if n<=0:
            return True
        return False
        