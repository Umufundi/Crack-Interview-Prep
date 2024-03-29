class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def valid(s):
            l,r=0,0
            for c in s:
                if c=='(':l+=1
                elif c==')':
                    if  l<=0:r+=1
                    else:l-=1
            return not l and not r
        res=[];seen=set();level={s}
        while True:
            newLevel=set()
            for word in level:
                if valid(word):res.append(word)
            if res: return res 
            for word in level:
                for i in range(len(word)):
                    if word[i] in '()':
                        newWord=word[:i]+word[i+1:];
                        if newWord not in seen:seen.add(newWord);newLevel.add(newWord)       
            level=newLevel        
        return [""]