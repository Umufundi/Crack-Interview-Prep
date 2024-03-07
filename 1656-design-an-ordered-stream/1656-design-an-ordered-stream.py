class OrderedStream:
    def __init__(self, n: int):
      self.arr = [None]*n 
      self.ptr = 0 
    
    def get_chunk(self):  
      chunk = []
      while self.ptr < len(self.arr) and self.arr[self.ptr]:
        chunk.append(self.arr[self.ptr])
        self.ptr+=1 
      return chunk
    
    def insert(self, idKey: int, value: str) -> List[str]:
      
      self.arr[idKey-1] = value
      return self.get_chunk() 