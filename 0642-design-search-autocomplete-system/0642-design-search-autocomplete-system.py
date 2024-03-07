class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.hashmap = {x:y for x,y in zip(sentences,times)};self.stack = [[x,y] for x,y in zip(list(self.hashmap), list(self.hashmap.values()))];self.stack.sort(key= lambda x: (-x[1], x[0]));self.usr_input = ''
    def input(self, c: str) -> List[str]:
        path=[];counter=0
        if c == '#':
          if self.usr_input not in self.hashmap:self.hashmap[self.usr_input] = 1
          else:self.hashmap[self.usr_input] += 1
          self.stack = [[x,y] for x,y in zip(list(self.hashmap), list(self.hashmap.values()))];self.stack.sort(key= lambda x: (-x[1], x[0]));self.usr_input = '';return []
        self.usr_input += c
        for i in range(len(self.stack)):
            if self.stack[i][0].startswith(self.usr_input):path.append(self.stack[i][0]);counter += 1
            if counter == 3 or i == len(self.stack) - 1:
                break
        return path
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)