class textfile:
       ntfiles = 0  # count of number of textfile objects
   def __init__(self,fname):
      textfile.ntfiles += 1
      self.myrank = textfile.ntfiles
      self.name = fname  # name 
      self.fh = open(fname)  # handle for the file
      self.lines = self.fh.readlines()
      self.nlines = len(self.lines)  # number of lines 
      self.nwords = 0  # number of words
   # omitting wordcount(), grep() for brevity

# create test files x and y
f = open('x','w')
f.write('abc\nde\n')
f = open('y','w')
f.write('12\n888\n')
a = textfile('x')
b = textfile('y')
print a.myrank  # prints 1
print b.myrank  # prints 2