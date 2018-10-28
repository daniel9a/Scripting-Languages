makeAscendNums <- function(x){ #class constructor for ascendNums
	#Check to make sure values in vector are in ascending order
	if(!all(diff(x) >= 0))  stop(" not nondecreasing")

	#Check if values in vector are strictly ascending
	strictVal <- FALSE
	if(all(diff(x) > 0)) strictVal <- TRUE

	if (length(x) != 0){
		value <- c(x)
		attr(value,"strictAscend") <- strictVal
		attr(value,"class") <- 'ascendNums'
	}
	#deal with null case
	else{
		value <- vector()
		attr(value,"strictAscend") <- strictVal
		attr(value,"class") <- 'ascendNums'
	}
	value
}

'[<-.ascendNums' <- function(ob,i,value){
	stop("read-only")	
}

'+.ascendNums' <-function(d1,d2){ #overloading + for ascendNums
	z <- c()

	a <- 1
	b <- 1

	#loop through vectors until one of the two is exhausted
	while(a <= length(d1) && b <= length(d2)){
		if(d1[a] > d2[b]){
			z <- c(z,d2[b])
			b <- b + 1
		}
		else{
			z <- c(z,d1[a])
			a <- a + 1
		}	
	}

	#add remaining elements of non-exhausted vector to output
	while(a <= length(d1)){
		z <- c(z,d1[a])
	       	a <- a + 1	
	}

	while(b <= length(d2)){
		z <- c(z,d2[b])
	       	b <- b + 1	
	}

	#output class
	makeAscendNums(z)	
}

