class OrderedStream:

    def __init__(self, n: int):
      self.arr = [None]*n # initialize the array for size n
      self.ptr = 0 # remeber where the stream pointer is at
    def get_chunk(self):
      chunk = []

      # Construct the next chunk by checking bounds, and ensuring value is not None
      while self.ptr < len(self.arr) and self.arr[self.ptr]:
        chunk.append(self.arr[self.ptr])
        self.ptr+=1 # Update the pointer
      return chunk
    def insert(self, idKey: int, value: str) -> List[str]:
      # set the arr's 0-indexed value to the incoming value
      self.arr[idKey-1] = value
      return self.get_chunk() # then return the chunk