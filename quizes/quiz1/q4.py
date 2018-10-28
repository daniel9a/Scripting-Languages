class ulist(list):
       def __init__(self,x):
      self.x = uniq(x)
      list.__init__(self)
   def __add__(self,y):
      tmp = self.x + y
      return ulist(tmp)

u = [5,12,13,12,8]
u1 = ulist(u)
v1 = u1 + [2,1,8,8]
print v1.x