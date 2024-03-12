from collections import Counter
from operator import itemgetter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Count the frequency of each character
        frequency = Counter(s)
        
        # Sort the characters by frequency in descending order
        sorted_characters = sorted(frequency.items(), key=itemgetter(1), reverse=True)
        
        # Build the result string
        result = ''.join(char * freq for char, freq in sorted_characters)
        
        return result
