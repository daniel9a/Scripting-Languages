findAllKths <- function(m,k) 
{ 
   kthLarge <- function(x) sort(x)[length(x)-k+1]
   apply(m,1,kthLarge)
}

m <- matrix(c(5,8,2,6,9,12,1,4,16,1,18,5),nrow=4)
print(findAllKths(m,2)) # 9,8,2,5