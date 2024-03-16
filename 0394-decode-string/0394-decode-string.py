class Solution:
    def decodeString(self, s: str) -> str:
        curr_num = 0
        res = ""
        stack = []
        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)  # for numbers greater than 9
            elif c == '[':
                stack.append(curr_num)
                stack.append(res)
                curr_num = 0
                res = ""
            elif c == ']':
                prev_str = stack.pop()
                prev_num = stack.pop()
                res = prev_str + res * prev_num
            else:
                res += c
        return res