def accumulate(fl,m,c):
       f = open(fl)
   accumSum = 0
   k = 1
   while accumSum < m*c:
      num = f.readline()
      if num == '': return 
      num = int(num)
      accumSum += num
      if accumSum >= k*c:
         k += 1
         yield accumSum

try:
   g = open('v','w')
   g.writelines('5\n12\n13\n8\n88\n')
   g.close()
except:
   pass

acc = accumulate('v',6,6)
for r in acc: print r  # prints 17,30,38, one number per line