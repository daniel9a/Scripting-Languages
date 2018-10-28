class dirColl(list):
       def __init__(self,dirList):   
      self.dirList = dirList
      self.numDirs = len(dirList)
      self.i = 0  # indexes the collection
   def __iter__(self): return self
   def next(self):
      if self.i == self.numDirs: raise StopIteration
      thisDir = self.dirList[self.i]
      if not os.path.isdir(thisDir):
         print thisDir, ' is not a directory'
         raise StopIteration
      self.i += 1
      return thisDir

import os

try: 
   os.mkdir('x')
except: 
   pass
try: 
   os.mkdir('y')
except: 
   pass
try: 
   f = open('z','w')
   f.writelines('123\n')
   f.close()
except:
   pass

dc = dirColl(['x','y'])
for d in dc: print d  # prints 'x', 'y'

dc1 = dirColl(['x','z','y'])
for d in dc1: print d  # prints 'x', then error