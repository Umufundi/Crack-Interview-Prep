class Solution:
    def intToRoman(self, num: int) -> str:
        self.roman=''
    
        for i, magnitude in enumerate([1000, 100, 10, 1]):
            factor= int(num /magnitude)
            num = num %magnitude
            self.roman+= self.get_letter(factor, i)

        return self.roman

    def get_letter(self, factor, i):
        letters= ['M','C', 'X', 'I']
        letters5= ['','D', 'L', 'V']
        if factor<4:
            return letters[i]*factor
        elif factor==4:
            return letters[i]+letters5[i]
        elif factor>=5 and factor<9:
            return letters5[i]+ (factor-5)*letters[i]
        elif factor==9:
            return letters[i]+letters[i-1]