makeVecPos <- function(x)
{
    if (any(x <= 0)) stop('must be all-positive')
    class(x) <- 'vecPos'
    x
}

">.vecPos" <- function(xvp,yvp)
{
   all(as.vector(xvp) > as.vector(yvp))
}

u <- c(5,12,13)
v <- c(1,88,8)
w <- c(2,11,11)
uvp <- makeVecPos(u)
vvp <- makeVecPos(v)
wvp <- makeVecPos(w)
print(uvp)
print(uvp > vvp)
print(uvp > wvp)

try:
  {
  z <- c(0,88,8)
  zvp <- makeVecPos(z)
  }
