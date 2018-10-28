class cqIdxed:
   def __init__(self,q):
      self.q = q
      self.idx = 0
      self.lenQ = len(self.q)
   def __iter__(self): return self
   def next(self):
      tmp = self.q[self.idx]
      self.idx += 1
      if self.idx >= self.lenQ: self.idx = 0
      return tmp

myQ = cqIdxed([5,12,13])
i = 0
for qElement in myQ:
   print qElement
   i += 1
   if i >= 5: break