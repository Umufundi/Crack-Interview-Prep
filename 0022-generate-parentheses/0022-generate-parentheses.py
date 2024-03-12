class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def solver(op,cl,str):
            if op==0 and cl==0:
                output.append(str)
                return
            if op!=0:
                res1=str
                res1+='('
                solver(op-1,cl,res1)
            if cl>op:
                res2=str
                res2+=')'
                solver(op,cl-1,res2)
        open=n
        close=n
        str=''
        output=[]
        solver(open,close,str)
        return output