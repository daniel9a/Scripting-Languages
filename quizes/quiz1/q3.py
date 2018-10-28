def uniq(x):
       tmp = []
   for xelt in x:
      if not xelt in tmp:
         tmp.append(xelt)
   return tmp

u = [5,12,13,12,8]
print uniq(u)