class Solution:
    def isValid(self, s: str) -> bool:
        
        
        # initialize a stack
        pile = []
        # match brackets together
        matches = {")":"(",
                  "]":"[",
                  "}":"{"}
        # iterate through the string 
        for i in s:
        # push opening brackets only in the stack
            if i in matches.values():
                pile.append(i)
        # pop only when the closing bracket matches stack[-1]
            elif i in matches:
                if not pile or pile.pop() != matches[i]:
                    return False
        # return whether the stack exist or not
        return not pile
        