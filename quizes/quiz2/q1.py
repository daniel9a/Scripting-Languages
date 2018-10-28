# class to store (grayscale) images

# image object constructed from 2-D array, each element being a row of
# nPixRow pixel value; range of values is 0-k, in order of increasing
# brightness 

# actions upon instantiation: 

#    an instance variable Rows will be formed, a copy of imgRows

#    an instance variable errRows will be formed, a boolean list 
#    indicating rows whose length is not nPixRow; another instance
#    variables, nBad, will contain the number of offending rows

#    an instance variable imgRowMajor will be formed, containing the
#    the pixel values as a one dimensional array, stored row-by-row; if
#    nBad > 0, this variable will have the value None

#    an instance variable hist will be formed, a list of length k+1
#    containing the counts of each brightness level; if  nBad > 0, this
#    variable will have the value None

class img():
   def __init__(self,imgRows,nPixRow,k):
      self.Rows = imgRows
      self.nCols = nPixRow
      self.nRows =len(imgRows)
      self.errRows = map(lambda row: len(row) != nPixRow,self.Rows)
      self.nBad = sum(self.errRows)
      if self.nBad == 0:
         self.imgRowMajor = reduce(lambda u,v:u+v,self.Rows)
         all0s = (k+1) * [0]
         def toIndicator(hist,pix):
            hist[pix] += 1
            return hist
         self.hist = reduce(toIndicator,self.imgRowMajor,all0s)
      else:
         self.imgRowMajor = None
         self.hist = None

pixels1 = [[2,0],[1,3],[1,1]]
img1 = img(pixels1,2,3)
print img1.nRows  # prints 3
print img1.imgRowMajor  # prints [2,0,1,3,1,1]
print img1.hist  # prints [1,3,1,1]
pixels2 = [[2,0,5],[1,3],[1,1]]
img2 = img(pixels2,2,3)
print img2.errRows  # prints [True,False,False]
print img2.imgRowMajor  # prints None
print img2.hist  # prints None
