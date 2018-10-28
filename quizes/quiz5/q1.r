f1 <- faithful[faithful[,1] > 3.25,]
print('number of durations > 3.25:')
print(nrow(f1))              
print('mean eruption duration for waits > 65:')
f2 <- faithful[faithful[,2] > 65,]
print(mean(f2[,1]))